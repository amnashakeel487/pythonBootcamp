"""
Scraper: fetches a product page and extracts (name, price).

Design notes
------------
- Uses a realistic User-Agent header so sites don't immediately 403 us.
- Detects the site (Amazon / Flipkart / generic) via regex on the URL,
  then dispatches to a site-specific parser. Each parser tries several
  known CSS selectors, because e-commerce sites frequently A/B test
  their markup — falling back gracefully instead of crashing is what
  makes this "industrial-level" rather than a toy script.
- A SeleniumScraper subclass is provided for JS-rendered pages. It is
  optional: if selenium/webdriver-manager aren't installed, importing
  this module still works fine — only instantiating SeleniumScraper
  would fail, with a clear error message.
"""

from __future__ import annotations

import os
import re
from typing import Optional, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import PriceNotFoundError, ScraperError

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Matches things like "Rs. 1,29,999.00", "$1,299.99", "129999", "PKR 45,000"
PRICE_PATTERN = re.compile(r"[\d]{1,3}(?:[,.\s]\d{2,3})*(?:\.\d{1,2})?")

# Domains whose entire purpose is to redirect somewhere else. If one of
# these specifically times out / refuses to connect, it's worth telling
# the user to try the expanded URL instead — these domains are sometimes
# blocked by corporate firewalls or antivirus tools as a phishing heuristic,
# independent of anything this app can control.
KNOWN_SHORTENERS = {"a.co", "amzn.to", "bit.ly", "tinyurl.com", "t.co", "goo.gl", "rebrand.ly"}


def _build_session(retries: int = 2) -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=retries,
        connect=retries,
        read=retries,
        backoff_factor=1.5,  # 0s, 1.5s, 3s between attempts
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


class Scraper:
    """Requests + BeautifulSoup based scraper with multi-site support."""

    def __init__(self, timeout: Optional[int] = None, retries: int = 2) -> None:
        self.timeout = timeout or int(os.getenv("SCRAPE_TIMEOUT_SECONDS", "15"))
        self.session = _build_session(retries=retries)

    # ------------------------------------------------------------------ #
    # Site detection (Bonus: Multi-URL support with Regex)
    # ------------------------------------------------------------------ #
    @staticmethod
    def detect_site(url: str) -> str:
        if re.search(r"amazon\.", url, re.IGNORECASE):
            return "amazon"
        if re.search(r"flipkart\.", url, re.IGNORECASE):
            return "flipkart"
        if re.search(r"daraz\.", url, re.IGNORECASE):
            return "daraz"
        return "generic"


    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def get_product_info(self, url: str) -> Tuple[str, float, str]:
        """
        Fetch `url` and return (product_name, price, detected_site).
        Raises ScraperError / PriceNotFoundError on failure — callers
        are expected to catch these and keep the monitoring loop alive.
        """
        try:
            response = self.session.get(url, headers=HEADERS, timeout=self.timeout, allow_redirects=True)
            response.raise_for_status()
        except requests.ConnectionError as exc:
            hostname = urlparse(url).hostname or ""
            if hostname in KNOWN_SHORTENERS:
                raise ScraperError(
                    f"Could not reach {hostname} after {self.session.adapters['https://'].max_retries.total + 1} "
                    f"attempts — this link-shortening service appears blocked or unreachable from your network "
                    f"(common with some firewalls/antivirus tools). Open the link in a browser, copy the "
                    f"expanded product URL after it redirects, and use that instead. Details: {exc}"
                ) from exc
            raise ScraperError(
                f"Could not connect to {url} — this is a network issue (DNS/firewall/offline), "
                f"not a parsing bug. Details: {exc}"
            ) from exc
        except requests.RequestException as exc:
            raise ScraperError(f"Request failed for {url}: {exc}") from exc

        # Detect the site from the FINAL URL (after following any redirects),
        # not the original one — this matters for shortened links like
        # a.co or amzn.to, which don't contain "amazon" themselves but
        # redirect to a real amazon.* URL that does.
        site = self.detect_site(response.url)

        # Defensive encoding handling: some servers omit a charset in the
        # Content-Type header, which makes requests fall back to a naive
        # guess (often Latin-1) and can corrupt multi-byte characters like
        # currency symbols — which in turn confuses the HTML parser and
        # can cause it to lose track of nearby tags entirely. Re-deriving
        # the encoding from the actual response bytes fixes that.
        if not response.encoding or response.encoding.lower() == "iso-8859-1":
            response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, "lxml")

        parser = {
            "amazon": self._parse_amazon,
            "flipkart": self._parse_flipkart,
            "daraz": self._parse_daraz,
        }.get(site, self._parse_generic)

        name, price = parser(soup)

        if price is None:
            raise PriceNotFoundError(f"Could not locate a price on {url}")

        return name or "Unknown product", price, site

    # ------------------------------------------------------------------ #
    # Site-specific parsers
    # ------------------------------------------------------------------ #
    def _parse_amazon(self, soup: BeautifulSoup) -> Tuple[Optional[str], Optional[float]]:
        name_el = soup.select_one("#productTitle")
        name = name_el.get_text(strip=True) if name_el else None

        price_selectors = [
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            "span.a-price span.a-offscreen",
            "#corePrice_feature_div span.a-offscreen",
        ]
        price = self._first_matching_price(soup, price_selectors)
        return name, price

    def _parse_flipkart(self, soup: BeautifulSoup) -> Tuple[Optional[str], Optional[float]]:
        name_el = soup.select_one("span.B_NuCI") or soup.select_one("h1 span")
        name = name_el.get_text(strip=True) if name_el else None

        price_selectors = ["div._30jeq3._16Jk6d", "div._30jeq3"]
        price = self._first_matching_price(soup, price_selectors)
        return name, price

    def _parse_daraz(self, soup: BeautifulSoup) -> Tuple[Optional[str], Optional[float]]:
        name_el = soup.select_one("h1.pdp-mod-product-badge-title")
        name = name_el.get_text(strip=True) if name_el else None

        price_selectors = ["span.pdp-price", "span.pdp-price_type_normal"]
        price = self._first_matching_price(soup, price_selectors)
        return name, price

    def _parse_generic(self, soup: BeautifulSoup) -> Tuple[Optional[str], Optional[float]]:
        """
        Best-effort fallback for arbitrary product pages: use the <title>
        tag as the name, and scan common price-ish CSS classes/ids, then
        finally the whole page text, for something that looks like a price.
        """
        title_el = soup.find("title")
        name = title_el.get_text(strip=True) if title_el else None

        candidates = soup.select(
            "[class*='price'], [id*='price'], [class*='Price'], [id*='Price']"
        )
        for el in candidates:
            price = self._extract_price(el.get_text())
            if price is not None:
                return name, price

        # last resort: search the raw page text
        return name, self._extract_price(soup.get_text())

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    def _first_matching_price(self, soup: BeautifulSoup, selectors: list) -> Optional[float]:
        for selector in selectors:
            el = soup.select_one(selector)
            if el:
                price = self._extract_price(el.get_text())
                if price is not None:
                    return price
        return None

    @staticmethod
    def _extract_price(text: str) -> Optional[float]:
        if not text:
            return None
        match = PRICE_PATTERN.search(text)
        if not match:
            return None
        raw = match.group().replace(",", "").replace(" ", "")
        try:
            return float(raw)
        except ValueError:
            return None


class SeleniumScraper(Scraper):
    """
    Optional headless-browser scraper for JavaScript-rendered pages.

    Only imports selenium when actually instantiated, so the rest of the
    app works fine even if selenium / a chromedriver aren't installed.
    """

    def __init__(self, timeout: int = 15) -> None:
        super().__init__(timeout=timeout)
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
        except ImportError as exc:
            raise ScraperError(
                "SeleniumScraper requires 'selenium' to be installed "
                "(pip install selenium webdriver-manager)."
            ) from exc

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument(f"user-agent={HEADERS['User-Agent']}")
        self._driver_cls = webdriver
        self._options = options

    def get_product_info(self, url: str) -> Tuple[str, float, str]:
        driver = self._driver_cls.Chrome(options=self._options)
        try:
            driver.set_page_load_timeout(self.timeout)
            driver.get(url)
            site = self.detect_site(driver.current_url)  # final URL after any redirects
            soup = BeautifulSoup(driver.page_source, "lxml")
        except Exception as exc:  # noqa: BLE001 - broad on purpose, see module docstring
            raise ScraperError(f"Selenium request failed for {url}: {exc}") from exc
        finally:
            driver.quit()

        parser = {
            "amazon": self._parse_amazon,
            "flipkart": self._parse_flipkart,
            "daraz": self._parse_daraz,
        }.get(site, self._parse_generic)

        name, price = parser(soup)
        if price is None:
            raise PriceNotFoundError(f"Could not locate a price on {url}")
        return name or "Unknown product", price, site

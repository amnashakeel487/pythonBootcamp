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

import re
from typing import Optional, Tuple

import requests
from bs4 import BeautifulSoup

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


class Scraper:
    """Requests + BeautifulSoup based scraper with multi-site support."""

    def __init__(self, timeout: int = 10) -> None:
        self.timeout = timeout

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
        site = self.detect_site(url)

        try:
            response = requests.get(url, headers=HEADERS, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise ScraperError(f"Request failed for {url}: {exc}") from exc

        soup = BeautifulSoup(response.content, "html.parser")

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
        site = self.detect_site(url)
        driver = self._driver_cls.Chrome(options=self._options)
        try:
            driver.set_page_load_timeout(self.timeout)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
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

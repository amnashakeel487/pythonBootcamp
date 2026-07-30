"""
PriceGuard — Automated E-Commerce Price Tracker & Alert System
=================================================================
Entry point. Run with:  python main.py

Menu:
  1. Add new product to track
  2. View all tracked products
  3. Start the Price Monitoring bot
  4. Exit
"""

from __future__ import annotations

import os
import time
from datetime import datetime

from dotenv import load_dotenv

from src.alert_manager import AlertManager
from src.data_manager import DataManager
from src.exceptions import AlertError, PriceGuardError, ScraperError
from src.product import Product
from src.scraper import Scraper

load_dotenv()  # pulls EMAIL_SENDER, EMAIL_PASSWORD, etc. from .env

CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", "3600"))  # default 1 hour


# ---------------------------------------------------------------------- #
# Menu actions
# ---------------------------------------------------------------------- #
def add_product(data_manager: DataManager, scraper: Scraper) -> None:
    url = input("\nEnter product URL: ").strip()
    if not url:
        print("⚠️  URL cannot be empty.")
        return

    try:
        target_price = float(input("Enter your target price: Rs. ").strip())
    except ValueError:
        print("⚠️  Target price must be a number.")
        return

    print("🔎 Fetching current price to confirm the product... please wait.")
    try:
        name, price, site = scraper.get_product_info(url)
    except ScraperError as exc:
        print(f"⚠️  Could not fetch this product right now ({exc}). "
              f"Saving it anyway — it will be checked on the next scan.")
        name, price, site = "Unknown product (will update on next scan)", 0.0, scraper.detect_site(url)

    product = Product(url=url, name=name, target_price=target_price, site=site)
    if price > 0:
        product.update_price(price)
        data_manager.append_history(product)

    data_manager.add_product(product)
    print(f"✅ Added: {name}  (site: {site}, current price: Rs. {price:,.2f})")


def view_products(data_manager: DataManager) -> None:
    products = data_manager.load_products()
    if not products:
        print("\n📭 No products tracked yet. Choose option 1 to add one.")
        return

    print(f"\n📦 Tracking {len(products)} product(s):\n")
    print(f"{'NAME':45} | {'SITE':10} | {'LAST PRICE':>14} | {'TARGET':>14} | STATUS")
    print("-" * 105)
    for p in products:
        print(p)
    print()


def run_monitoring_bot(data_manager: DataManager, scraper: Scraper, alert_manager: AlertManager) -> None:
    print(f"\n🤖 PriceGuard bot started. Checking every {CHECK_INTERVAL_SECONDS} seconds. "
          f"Press Ctrl+C to stop.\n")
    try:
        while True:
            products = data_manager.load_products()
            if not products:
                print("📭 Nothing to track yet. Add a product first (Ctrl+C to go back to the menu).")

            for product in products:
                check_single_product(product, data_manager, scraper, alert_manager)

            print(f"\n😴 Sleeping for {CHECK_INTERVAL_SECONDS} seconds "
                  f"(next check at {_next_check_time()})...\n")
            time.sleep(CHECK_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\n⏹️  Monitoring stopped by user. Returning to menu.\n")


def check_single_product(
    product: Product,
    data_manager: DataManager,
    scraper: Scraper,
    alert_manager: AlertManager,
) -> None:
    """
    Scrape one product, persist the result, and fire an alert if needed.
    Any failure here is caught and logged — it must NEVER crash the loop.
    """
    try:
        name, price, site = scraper.get_product_info(product.url)
        product.name = name or product.name
        product.site = site

        previous_price = product.last_price
        product.update_price(price)
        data_manager.append_history(product)

        print(f"[{product.last_checked}] {product.name[:40]:40} -> Rs. {price:,.2f}")

        # Intelligent alert logic: only fire when price is below target
        # AND we haven't already alerted for this dip (Product.alert_sent).
        if product.is_below_target() and not product.alert_sent:
            history = data_manager.get_price_history(product)
            try:
                alert_manager.send_price_alert(product, history=history)
                product.alert_sent = True
                print(f"   📧 Alert sent for {product.name[:40]} "
                      f"(dropped to Rs. {price:,.2f}, target was Rs. {product.target_price:,.2f})")
            except AlertError as exc:
                print(f"   ⚠️  Alert failed to send: {exc}")

        data_manager.update_product(product)

    except ScraperError as exc:
        # Requirement 6: never crash — log and move on to the next product.
        print(f"⚠️  Scraping failed for {product.url} ({exc}). Retrying next cycle.")
    except PriceGuardError as exc:
        print(f"⚠️  Unexpected PriceGuard error for {product.url}: {exc}")


def _next_check_time() -> str:
    ts = time.time() + CHECK_INTERVAL_SECONDS
    return datetime.fromtimestamp(ts).strftime("%H:%M:%S")


# ---------------------------------------------------------------------- #
# CLI
# ---------------------------------------------------------------------- #
def print_banner() -> None:
    print(r"""
  ____        _          ____                     _
 |  _ \ _ __(_) ___ ___ / ___|_   _  __ _ _ __ __| |
 | |_) | '__| |/ __/ _ \ |  _| | | |/ _` | '__/ _` |
 |  __/| |  | | (_|  __/ |_| | |_| | (_| | | | (_| |
 |_|   |_|  |_|\___\___|\____|\__,_|\__,_|_|  \__,_|

 Automated E-Commerce Price Tracker & Alert System
""")


def main() -> None:
    data_manager = DataManager()
    scraper = Scraper()
    alert_manager = AlertManager()

    print_banner()

    while True:
        print("1. Add new product to track")
        print("2. View all tracked products")
        print("3. Start the Price Monitoring bot")
        print("4. Exit")
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            add_product(data_manager, scraper)
        elif choice == "2":
            view_products(data_manager)
        elif choice == "3":
            run_monitoring_bot(data_manager, scraper, alert_manager)
        elif choice == "4":
            print("👋 Goodbye! Stay guarded.")
            break
        else:
            print("⚠️  Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()

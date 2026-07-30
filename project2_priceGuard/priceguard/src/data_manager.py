"""
DataManager: all CSV file I/O lives here.

Two kinds of files are managed:
  1. data/products.csv        -> one row per tracked product (current state)
  2. data/history/<slug>.csv  -> one row per price check for that product
                                  (used to draw the price-history graph)
"""

from __future__ import annotations

import csv
import os
import re
from datetime import datetime
from typing import List

from .exceptions import DataPersistenceError
from .product import Product

PRODUCTS_FIELDNAMES = [
    "url", "name", "site", "target_price", "last_price",
    "highest_price", "lowest_price", "last_checked", "alert_sent",
]

HISTORY_FIELDNAMES = ["timestamp", "price"]


class DataManager:
    def __init__(
        self,
        products_file: str = "data/products.csv",
        history_dir: str = "data/history",
    ) -> None:
        self.products_file = products_file
        self.history_dir = history_dir
        os.makedirs(os.path.dirname(self.products_file) or ".", exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)
        self._ensure_products_file_exists()

    # ------------------------------------------------------------------ #
    # products.csv
    # ------------------------------------------------------------------ #
    def _ensure_products_file_exists(self) -> None:
        if not os.path.exists(self.products_file):
            with open(self.products_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=PRODUCTS_FIELDNAMES)
                writer.writeheader()

    def load_products(self) -> List[Product]:
        try:
            with open(self.products_file, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [Product.from_dict(row) for row in reader if row.get("url")]
        except OSError as exc:
            raise DataPersistenceError(f"Could not read {self.products_file}: {exc}") from exc

    def save_products(self, products: List[Product]) -> None:
        try:
            with open(self.products_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=PRODUCTS_FIELDNAMES)
                writer.writeheader()
                for product in products:
                    writer.writerow(product.to_dict())
        except OSError as exc:
            raise DataPersistenceError(f"Could not write {self.products_file}: {exc}") from exc

    def add_product(self, product: Product) -> None:
        products = self.load_products()
        products.append(product)
        self.save_products(products)

    def update_product(self, updated: Product) -> None:
        products = self.load_products()
        for i, p in enumerate(products):
            if p.url == updated.url:
                products[i] = updated
                break
        else:
            products.append(updated)
        self.save_products(products)

    # ------------------------------------------------------------------ #
    # per-product price history (used for the matplotlib graph)
    # ------------------------------------------------------------------ #
    @staticmethod
    def _slugify(name: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()
        return slug[:60] or "product"

    def _history_path(self, product: Product) -> str:
        return os.path.join(self.history_dir, f"{self._slugify(product.name)}.csv")

    def append_history(self, product: Product) -> None:
        path = self._history_path(product)
        file_exists = os.path.exists(path)
        try:
            with open(path, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=HISTORY_FIELDNAMES)
                if not file_exists:
                    writer.writeheader()
                writer.writerow({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "price": product.last_price,
                })
        except OSError as exc:
            raise DataPersistenceError(f"Could not write history for {product.name}: {exc}") from exc

    def get_price_history(self, product: Product) -> List[tuple]:
        path = self._history_path(product)
        if not os.path.exists(path):
            return []
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [(row["timestamp"], float(row["price"])) for row in reader]

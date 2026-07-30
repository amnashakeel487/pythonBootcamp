"""
Product: a single item being tracked by PriceGuard.

This is a plain data-holding class (an OOP "model") that knows how to
serialize/deserialize itself to and from a CSV row. It does not know
anything about scraping, emailing, or file I/O — that separation of
concerns is what keeps the codebase testable and industry-grade.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Product:
    url: str
    name: str
    target_price: float
    site: str = "unknown"
    last_price: float = 0.0
    highest_price: float = 0.0
    lowest_price: float = 0.0
    last_checked: str = ""
    alert_sent: bool = False  # True once an alert has fired for the *current* dip

    # ------------------------------------------------------------------ #
    # Derived helpers
    # ------------------------------------------------------------------ #
    def is_below_target(self) -> bool:
        """Return True if the last known price beats the user's target."""
        return self.last_price > 0 and self.last_price < self.target_price

    def drop_percentage(self, reference_price: float) -> float:
        """
        % drop of last_price relative to a reference price
        (typically the highest price ever recorded, or the previous price).
        """
        if reference_price <= 0:
            return 0.0
        return round((reference_price - self.last_price) / reference_price * 100, 2)

    def update_price(self, new_price: float) -> None:
        """Update tracking fields after a fresh scrape."""
        self.last_price = new_price
        self.last_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.highest_price == 0.0 or new_price > self.highest_price:
            self.highest_price = new_price
        if self.lowest_price == 0.0 or new_price < self.lowest_price:
            self.lowest_price = new_price

        # Smart alert reset: once price recovers above target,
        # allow a fresh alert the next time it dips again.
        if new_price >= self.target_price:
            self.alert_sent = False

    # ------------------------------------------------------------------ #
    # (De)serialization for CSV storage
    # ------------------------------------------------------------------ #
    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "name": self.name,
            "site": self.site,
            "target_price": self.target_price,
            "last_price": self.last_price,
            "highest_price": self.highest_price,
            "lowest_price": self.lowest_price,
            "last_checked": self.last_checked,
            "alert_sent": self.alert_sent,
        }

    @staticmethod
    def from_dict(row: dict) -> "Product":
        return Product(
            url=row["url"],
            name=row.get("name", "Unknown product"),
            target_price=float(row.get("target_price", 0) or 0),
            site=row.get("site", "unknown"),
            last_price=float(row.get("last_price", 0) or 0),
            highest_price=float(row.get("highest_price", 0) or 0),
            lowest_price=float(row.get("lowest_price", 0) or 0),
            last_checked=row.get("last_checked", ""),
            alert_sent=str(row.get("alert_sent", "False")).strip().lower() == "true",
        )

    def __str__(self) -> str:
        status = "🟢 BELOW TARGET" if self.is_below_target() else "—"
        return (
            f"{self.name[:45]:45} | {self.site:10} | "
            f"Rs.{self.last_price:>10,.2f} | Target: Rs.{self.target_price:>10,.2f} | "
            f"{status}"
        )

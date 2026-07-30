"""
AlertManager: sends Email (SMTP) and optional SMS (Twilio) notifications.

Security note
--------------
No credentials are hardcoded. Everything is read from environment
variables (see .env.example), loaded via python-dotenv in main.py and
read here with os.getenv(). This is the industry-standard way to keep
secrets out of source control.

Bonus features implemented here
--------------------------------
- Price-drop percentage in the alert subject/body
  (e.g. "🚨 15% Price Drop! Buy now!")
- A matplotlib line graph of price history, attached to the email.
"""

from __future__ import annotations

import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional, Tuple

import matplotlib
matplotlib.use("Agg")  # headless backend — no display server needed
import matplotlib.pyplot as plt

from .exceptions import AlertError
from .product import Product

# Twilio is optional — importing this module must not fail if it's absent.
try:
    from twilio.rest import Client as TwilioClient
    TWILIO_AVAILABLE = True
except ImportError:
    TWILIO_AVAILABLE = False


class AlertManager:
    def __init__(self) -> None:
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.sender_email = os.getenv("EMAIL_SENDER")
        self.sender_password = os.getenv("EMAIL_PASSWORD")
        self.receiver_email = os.getenv("EMAIL_RECEIVER", self.sender_email)

        self.twilio_sid = os.getenv("TWILIO_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_from_number = os.getenv("TWILIO_FROM_NUMBER")
        self.twilio_to_number = os.getenv("TWILIO_TO_NUMBER")

    # ------------------------------------------------------------------ #
    # Bonus: drop-percentage calculation
    # ------------------------------------------------------------------ #
    @staticmethod
    def calculate_drop_percentage(reference_price: float, current_price: float) -> float:
        if reference_price <= 0:
            return 0.0
        return round((reference_price - current_price) / reference_price * 100, 2)

    # ------------------------------------------------------------------ #
    # Bonus: matplotlib price-history graph, saved to a temp PNG
    # ------------------------------------------------------------------ #
    @staticmethod
    def generate_price_graph(product: Product, history: List[Tuple[str, float]]) -> Optional[str]:
        if len(history) < 2:
            return None  # not enough points to plot a trend yet

        timestamps = [row[0] for row in history]
        prices = [row[1] for row in history]

        fig, ax = plt.subplots(figsize=(7, 3.5), dpi=150)
        ax.plot(timestamps, prices, marker="o", linewidth=2, color="#4F46E5")
        ax.axhline(product.target_price, color="#10B981", linestyle="--", label="Target price")
        ax.set_title(f"Price history — {product.name[:40]}", fontsize=11)
        ax.set_ylabel("Price")
        ax.legend()
        ax.tick_params(axis="x", rotation=45, labelsize=7)
        fig.tight_layout()

        os.makedirs("data/history", exist_ok=True)
        output_path = os.path.join("data", "history", "_last_alert_graph.png")
        fig.savefig(output_path)
        plt.close(fig)
        return output_path

    # ------------------------------------------------------------------ #
    # Email
    # ------------------------------------------------------------------ #
    def send_price_alert(
        self,
        product: Product,
        history: Optional[List[Tuple[str, float]]] = None,
    ) -> None:
        if not self.sender_email or not self.sender_password:
            raise AlertError(
                "EMAIL_SENDER / EMAIL_PASSWORD are not set. "
                "Check your .env file (see .env.example)."
            )

        drop_pct = self.calculate_drop_percentage(product.highest_price, product.last_price)
        big_drop = drop_pct >= 10.0

        subject = (
            f"🚨 {drop_pct}% Price Drop! Buy now! — {product.name[:60]}"
            if big_drop
            else f"✅ Price Alert: {product.name[:60]} hit your target"
        )

        body = (
            f"Good news! The product you're tracking has dropped below your target price.\n\n"
            f"Product:        {product.name}\n"
            f"Current price:  Rs. {product.last_price:,.2f}\n"
            f"Target price:   Rs. {product.target_price:,.2f}\n"
            f"Price drop:     {drop_pct}% (from the highest recorded price of Rs. {product.highest_price:,.2f})\n"
            f"Link:           {product.url}\n\n"
        )
        if big_drop:
            body += "🚨 This is a significant drop of over 10%. Buy now! 🚨\n\n"
        body += "— Sent automatically by PriceGuard"

        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Bonus: attach the price-history graph, if we have enough data
        graph_path = None
        if history:
            graph_path = self.generate_price_graph(product, history)
        if graph_path and os.path.exists(graph_path):
            with open(graph_path, "rb") as img_file:
                image = MIMEImage(img_file.read())
                image.add_header("Content-Disposition", "attachment", filename="price_history.png")
                message.attach(image)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=15) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
        except smtplib.SMTPException as exc:
            raise AlertError(f"Failed to send email: {exc}") from exc

    # ------------------------------------------------------------------ #
    # Bonus: SMS via Twilio (optional)
    # ------------------------------------------------------------------ #
    def send_sms_alert(self, product: Product) -> None:
        if not TWILIO_AVAILABLE:
            raise AlertError("twilio package is not installed (pip install twilio).")
        if not all([self.twilio_sid, self.twilio_auth_token, self.twilio_from_number, self.twilio_to_number]):
            raise AlertError("Twilio credentials are missing from .env — SMS alert skipped.")

        drop_pct = self.calculate_drop_percentage(product.highest_price, product.last_price)
        text = (
            f"PriceGuard: {product.name[:40]} dropped {drop_pct}% to Rs.{product.last_price:,.2f} "
            f"(target Rs.{product.target_price:,.2f}). {product.url}"
        )
        try:
            client = TwilioClient(self.twilio_sid, self.twilio_auth_token)
            client.messages.create(
                body=text, from_=self.twilio_from_number, to=self.twilio_to_number
            )
        except Exception as exc:  # noqa: BLE001 - Twilio raises its own broad exceptions
            raise AlertError(f"Failed to send SMS: {exc}") from exc

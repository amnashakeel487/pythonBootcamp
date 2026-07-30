# PriceGuard: Automated E-Commerce Price Tracker & Alert System

This is an automated Price Tracking Bot used for E-Commerce price surveillance.
It watches product pages you care about, checks their price on a schedule, and
emails you the moment the price drops below a target you set — with a price-history
graph attached.

---

## ✨ Features

- **Pure OOP architecture** — `Product`, `Scraper`, `DataManager`, and `AlertManager`
  each have a single, well-defined responsibility.
- **Multi-site web scraping** with `requests` + `BeautifulSoup`, using realistic
  browser headers so requests aren't immediately blocked.
- **Regex-based site detection** — automatically recognizes Amazon, Flipkart, and
  Daraz URLs and applies the right parsing logic for each; falls back to a generic
  price-scanning parser for any other site.
- **Optional Selenium mode** (`SeleniumScraper`) for JavaScript-heavy pages, running
  fully headless.
- **CSV persistence** — `data/products.csv` tracks every product's current state;
  `data/history/<product>.csv` keeps a full price-history log per product.
- **Automated scheduling loop** — checks every product on a configurable interval
  (default: every hour) via `time.sleep()`.
- **Intelligent alert logic** — alerts fire only the *first* time a price crosses
  below target, not on every single check, so you don't get spammed.
- **Robust error handling** — a failed request, a down website, or a missing price
  never crashes the bot; it logs the failure and keeps monitoring everything else.
- **Interactive CLI menu** for adding products, viewing your tracked list, and
  starting the monitoring bot.

### 🏆 Bonus features

- **Price-drop percentage alerts** — if a product has dropped 10% or more from its
  highest recorded price, the email subject reads `🚨 X% Price Drop! Buy now!`
- **Email with graph attachment** — a `matplotlib` line chart of the full price
  history (with your target price marked) is generated and attached to every alert.
- **Optional SMS alerts** via Twilio.

---

## 🏗️ Architecture

```
priceguard/
├── main.py                  # CLI entry point + scheduling loop
├── requirements.txt
├── .env.example              # template for secrets (copy to .env)
├── .gitignore
├── src/
│   ├── product.py            # Product — data model + price/alert logic
│   ├── scraper.py             # Scraper / SeleniumScraper — fetch + parse price
│   ├── data_manager.py        # DataManager — CSV read/write, price history
│   ├── alert_manager.py       # AlertManager — SMTP email, Twilio SMS, graphs
│   └── exceptions.py          # Custom exception hierarchy
└── data/
    ├── products.csv           # current state of every tracked product
    └── history/                # per-product price-history CSVs (for graphs)
```

**Flow:** `main.py` loads products via `DataManager` → asks `Scraper` for a fresh
price → updates the `Product` object → appends to price history → if the price is
below target and hasn't already been alerted on, asks `AlertManager` to send an
email (with a `matplotlib` graph attached) → saves everything back to CSV → sleeps
→ repeats.

---

## ⚙️ Setup

```bash
git clone <this-repo-url>
cd priceguard
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then edit .env with your real Gmail app password, etc.
```

### Gmail App Password
Regular Gmail passwords won't work with SMTP. Create an **App Password** at
https://myaccount.google.com/apppasswords and put it in `.env` as `EMAIL_PASSWORD`.

### Run it

```bash
python main.py
```

```
1. Add new product to track
2. View all tracked products
3. Start the Price Monitoring bot
4. Exit
```

---

## 🔐 Environment Variables

No secrets are ever hardcoded — everything sensitive is read via `os.getenv()`
from a local `.env` file (which is git-ignored). See `.env.example` for the full
list of variables (email credentials, SMTP settings, check interval, optional
Twilio SMS credentials).

---

## 🖼️ Screenshots

> _Add these once you run the project locally:_
- `docs/cli_menu.png` — the interactive CLI menu in action
- `docs/email_alert.png` — an example price-drop email with the attached graph

---

## ⚠️ Disclaimer

This project is for educational / personal-automation purposes. Scraping
e-commerce sites may be against their Terms of Service — check the target
site's `robots.txt` and ToS, add reasonable delays between requests, and prefer
official APIs where available before deploying this against production traffic.

---

## 🛠️ Tech Stack

`Python 3.10+` · `requests` · `BeautifulSoup4` · `Selenium` (optional) ·
`smtplib` · `matplotlib` · `python-dotenv` · `csv`

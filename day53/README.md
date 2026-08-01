# 🏠 Zillow Data Entry Automation Bot

This project automates the process of collecting property listings from Zillow and submitting them into a Google Form. It combines web scraping with browser automation to eliminate repetitive manual data entry.

## Features

- Scrapes property addresses
- Extracts prices
- Collects property links
- Automatically fills Google Forms
- Uses BeautifulSoup for scraping
- Uses Selenium for browser automation

## Technologies Used

- Python
- BeautifulSoup
- Selenium
- Requests
- WebDriver Manager

## Project Structure

```
day53/
│
├── main.py
├── scraper.py
├── form_filler.py
├── config.py
├── README.md
├── requirements.txt
├── .gitignore
└── data/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Learning Outcomes

- Web Scraping with BeautifulSoup
- CSS Selectors
- Selenium Form Automation
- Requests Library
- Data Processing
- Automation Workflows

## Note

Zillow frequently updates its HTML structure and may block automated requests. If scraping fails, save the webpage locally (`zillow.html`) and update the scraper to parse that local file instead of making a live request.
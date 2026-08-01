# 🏠 Zillow Data Entry Automation Bot

This project automates the process of collecting property listings from Zillow and submitting them into a Google Form. It combines web scraping with browser automation to eliminate repetitive manual data entry.

<img width="1917" height="1077" alt="1" src="https://github.com/user-attachments/assets/dadc26b9-7e2e-44a1-b11b-bf29325f4c28" />
<img width="1917" height="1077" alt="2" src="https://github.com/user-attachments/assets/fbd63397-e258-47ca-be73-25c2451c09bc" />


# spreedsheet of reponse
https://docs.google.com/spreadsheets/d/1XaiAcu47Z7tuG81DuwEQ1Mg6b9COEy-hmH4_iHUiaOA/edit?usp=sharing

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

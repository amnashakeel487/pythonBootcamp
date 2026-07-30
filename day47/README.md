# 🛒 Day 47 - Automated Amazon Price Tracker

## 📌 Project Overview

The Automated Amazon Price Tracker is a Python automation project that monitors the price of a product on Amazon. It uses the Requests library to fetch the webpage and BeautifulSoup to parse the HTML and extract the product title and current price. If the product price drops below a predefined target price, the application automatically sends an email notification to the user.

This project demonstrates how web scraping and email automation can be combined to solve a real-world problem.

---

## 🚀 Features

- Scrapes product information from an Amazon product page.
- Extracts the product title and current price.
- Compares the current price with a target price.
- Sends an automatic email alert when the price drops.
- Uses custom HTTP headers to simulate a browser request.
- Demonstrates real-world web scraping automation.

---

## 🛠 Technologies Used

- Python 3
- Requests
- BeautifulSoup4 (bs4)
- smtplib
- lxml / html.parser
- Visual Studio Code or PyCharm

---

## 📚 Concepts Covered

- Web Scraping
- HTTP Requests
- HTML Parsing
- BeautifulSoup
- CSS Selectors
- Request Headers
- Email Automation
- SMTP
- Error Handling
- Automation with Python

---

## 📂 Project Structure

```
Day47/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

1. Clone the repository.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

or

```bash
pip install beautifulsoup4 requests lxml
```

3. Open `config.py` and update:

- Amazon Product URL
- Target Price
- Email Address
- App Password

4. Run the project:

```bash
python main.py
```

---

## 🎯 Learning Outcomes

After completing this project, I can:

- Send HTTP requests to websites.
- Parse HTML using BeautifulSoup.
- Extract specific webpage elements.
- Compare extracted data using Python.
- Automate email notifications.
- Build a real-world web scraping application.
- Understand common challenges of scraping modern websites.

---

## ⚠️ Note

Amazon uses advanced anti-bot protection (AWS WAF), which may block automated requests made with the Requests library. Because of this, the scraper may not always retrieve the actual product page. This project is intended for educational purposes to practice web scraping concepts. For modern websites with dynamic content or anti-bot protection, browser automation tools such as Selenium or Playwright are often more reliable.

---

## 👩‍💻 Author

**Amna Shakeel**

Completed as part of the **100 Days of Python Bootcamp**.
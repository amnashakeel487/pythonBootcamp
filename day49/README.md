# 💼 Day 49 – LinkedIn Job Search Automation

## 📌 Project Overview

This project demonstrates browser automation using Selenium by logging into LinkedIn and navigating to job search results based on predefined keywords and location. It focuses on automating repetitive navigation tasks while reinforcing Selenium concepts such as locating elements, interacting with forms, and managing browser sessions.

> **Educational Note:** This project is intended for learning Selenium automation. Automated interaction with LinkedIn should always comply with LinkedIn's Terms of Service.

---

## 🚀 Features

- Launches Chrome automatically
- Logs into LinkedIn
- Searches for jobs using custom keywords
- Navigates through job listings
- Uses environment variables to protect credentials

---

## 🛠 Technologies Used

- Python
- Selenium
- python-dotenv

---

## 📚 Concepts Covered

- Selenium WebDriver
- Browser Automation
- Login Forms
- CSS Selectors
- XPath
- Environment Variables
- Exception Handling

---

## 📂 Project Structure

```
day49/
│
├── main.py
├── config.py
├── .env
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ Installation

```bash
pip install selenium python-dotenv
```

Create a `.env` file:

```text
LINKEDIN_EMAIL=your_email
LINKEDIN_PASSWORD=your_password
```

Run:

```bash
python main.py
```

---

## 🎯 Learning Outcomes

- Automate browser tasks with Selenium.
- Log into websites programmatically.
- Navigate dynamic web pages.
- Search and interact with online job listings.
- Build maintainable browser automation scripts.

---

## 👩‍💻 Author

**Amna Shakeel**

Completed as part of the **100 Days of Python Bootcamp**.
# 🛒 PriceGuard – Automated E-Commerce Price Tracker & Alert System

## 📌 Overview

PriceGuard is a Python command-line application that automatically tracks product prices from e-commerce websites. It periodically checks product prices and sends an email notification whenever a product reaches or falls below the user's target price.

The application is built using Object-Oriented Programming principles and demonstrates real-world automation techniques such as web scraping, scheduled monitoring, CSV data management, and email notifications.

---

<img width="1262" height="620" alt="image" src="https://github.com/user-attachments/assets/23928170-00ea-478f-a996-30a618b81a29" />


# ✨ Features

* Track multiple products simultaneously
* Add new products to monitor
* View all tracked products
* Automatically scrape product prices
* Compare current price with target price
* Send email alerts when price drops
* Prevent duplicate notifications
* Save product data in CSV format
* Maintain complete price history
* Scheduled automated monitoring
* Robust error handling
* Modular OOP architecture

---

# 🛠 Technologies Used

* Python 3
* BeautifulSoup4
* Requests
* Selenium (Optional)
* SMTP
* CSV
* Datetime
* Time
* OOP (Object-Oriented Programming)

---

# 📂 Project Structure

```
PriceGuard/
│
├── main.py
├── product.py
├── scraper.py
├── alert_manager.py
├── data_manager.py
├── products.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ⚙️ How It Works

1. Launch the application.
2. Add one or more product URLs.
3. Enter your desired target price.
4. Start the monitoring bot.
5. The application periodically checks product prices.
6. If the current price is below the target price:

   * An email notification is sent.
   * The alert is recorded to avoid duplicate emails.
7. Product information and price history are automatically saved to the CSV file.

---

# 📧 Email Notifications

Whenever a tracked product reaches the desired target price, PriceGuard automatically sends an email containing:

* Product Name
* Current Price
* Target Price
* Product URL
* Alert Message

---

# 📊 CSV Storage

All tracked products are stored in a CSV file containing information such as:

* Product Name
* Product URL
* Target Price
* Current Price
* Last Checked Time

The CSV file is automatically updated after each monitoring cycle.

---

# 🧱 Project Architecture

The application follows a modular Object-Oriented Programming architecture.

### Product

Stores all information related to a tracked product.

### Scraper

Retrieves product prices from e-commerce websites using web scraping.

### DataManager

Handles reading, writing, and updating product data in CSV files.

### AlertManager

Sends email notifications when the target price is reached.

### Main Application

Coordinates all modules and manages the monitoring workflow.

---

# 🚀 Future Improvements

* React Frontend Dashboard
* FastAPI Backend
* SQLite/PostgreSQL Database
* User Authentication
* SMS Notifications
* Price History Charts
* Multi-user Support
* Cloud Deployment
* Mobile-Friendly Interface

---

# 📚 Learning Outcomes

This project helped strengthen knowledge of:

* Object-Oriented Programming
* Web Scraping
* HTTP Requests
* File Handling
* CSV Data Management
* Email Automation
* Exception Handling
* Application Architecture
* Python Automation

---

# 👩‍💻 Author

**Amna Shakeel**

Python Developer | Software Engineering Student | Automation Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!

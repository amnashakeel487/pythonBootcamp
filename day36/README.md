# 📈 Day 36 – Stock Trading News Alert

## 📌 Project Overview

On Day 36 of the **100 Days of Python Bootcamp**, I built a Stock Trading News Alert application that combines multiple APIs to monitor stock prices and automatically notify users when significant market changes occur. The application retrieves stock market data, calculates price fluctuations, fetches the latest related news, and sends alerts using SMS.

This project demonstrates how different APIs can work together to automate real-world tasks.

---

## 🚀 Project Features

- Retrieve real-time stock price data using the Alpha Vantage API.
- Calculate daily percentage changes in stock prices.
- Detect significant stock movements based on a predefined threshold.
- Fetch the latest company-related news using the NewsAPI.
- Send automated SMS notifications using Twilio.
- Store API keys securely using environment variables.
- Parse and process JSON data from multiple APIs.
- Build an end-to-end automation workflow.

---

## 📚 Concepts Learned

- Working with multiple REST APIs
- Making HTTP requests using the Requests library
- Parsing JSON responses
- API Authentication
- Environment Variables (.env)
- Secure API Key Management
- Stock Price Analysis
- Percentage Calculations
- Conditional Logic
- SMS Automation with Twilio
- Python Automation Projects

---

## 🛠 Technologies Used

- Python 3
- Requests
- Python-dotenv
- Twilio
- Alpha Vantage API
- NewsAPI

---

## 📂 Project Structure

```
day36/
│
stock_alert
    ├── main.py
    └── README.md
```


## 📖 How It Works

1. Fetches the latest stock prices from Alpha Vantage.
2. Calculates the percentage difference between the last two trading days.
3. Checks if the price change exceeds the defined threshold.
4. Retrieves the latest news articles related to the company.
5. Sends an SMS containing the stock movement and top news headlines.

---

## 🎯 Learning Outcomes

By completing this project, I learned how to integrate multiple APIs into a single Python application, securely manage API credentials, analyze stock market data, retrieve real-time news, and automate notifications. This project strengthened my understanding of API integration and real-world Python automation.
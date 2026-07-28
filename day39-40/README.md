# ✈️ Flight Deal Finder & Flight Club (Day 39 & Day 40)

## 📌 Project Overview

This project is part of the **100 Days of Code: Python Bootcamp** and was completed across **Day 39** and **Day 40**.

On **Day 39**, I developed the core **Flight Deal Finder** application. The project retrieves destination information from Google Sheets, searches for available flights using a Flight Search API, compares the current ticket prices with predefined target prices, and identifies the best flight deals.

On **Day 40**, I enhanced the project by implementing the **Flight Club** feature. Users can now register to receive flight deal notifications, and the application automatically sends email alerts whenever a flight price falls below the target price. This transformed the project from a simple flight search application into a complete flight deal tracking and notification system.

This project demonstrates how multiple APIs, object-oriented programming, and automation can be combined to build a practical real-world Python application.

---

# Features

- Search for flight deals using live flight data.
- Read destination information from Google Sheets.
- Compare current flight prices with target prices.
- Automatically update missing IATA airport codes.
- Register users for flight notifications.
- Send email alerts when cheaper flights are found.
- Organize the project using object-oriented programming.
- Store API credentials securely using environment variables.

---

# Technologies Used

- Python 3
- Requests
- Datetime Module
- Python Dotenv
- Sheety API / Google Sheets API
- Tequila (Kiwi) Flight Search API
- SMTP (Email Notifications)
- Object-Oriented Programming (OOP)

---

# Project Structure

```
flight-deal-finder/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── user.py
├── .env
├── requirements.txt
└── README.md
```


# How It Works

1. Reads destination data from Google Sheets.
2. Retrieves missing airport IATA codes.
3. Searches for available flights.
4. Compares flight prices with target prices.
5. Registers users for Flight Club.
6. Sends email notifications when cheaper flights are found.

---

# Concepts Learned

- REST APIs
- JSON Handling
- API Authentication
- Object-Oriented Programming
- Working with Multiple Python Modules
- Environment Variables
- SMTP Email Automation
- Data Management
- Flight Search APIs
- Python Project Organization

---

# Learning Outcome

By completing this project, I learned how to build a complete Python application that integrates multiple APIs, manages external data sources, follows object-oriented design principles, and automates real-world tasks such as searching flight deals and sending email notifications.
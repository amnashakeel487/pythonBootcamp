# 🏃 Day 38 - Exercise Tracker with Python and Google Sheets

## 📌 Project Overview

This project is part of the **100 Days of Code: Python Bootcamp**.

The Exercise Tracker is a Python automation project that records daily workouts by integrating external APIs. Users can enter exercises in plain English, and the application automatically retrieves exercise details such as duration and calories burned before storing the data in a Google Sheet.

This project demonstrates how multiple APIs can work together to automate real-world tasks.

---

## 🚀 Features

- Accepts exercise input in natural language.
- Uses the Nutritionix API to analyze workout data.
- Retrieves exercise name, duration, and calories burned.
- Records workout details with the current date and time.
- Stores workout history in Google Sheets using the Sheety API (or Google Sheets API).
- Uses environment variables to securely manage API credentials.

---

## 🛠 Technologies Used

- Python 3
- Requests
- Datetime Module
- Nutritionix API
- Sheety API / Google Sheets API
- Environment Variables (.env)

---

## 📂 Project Structure

```
day38/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Configuration

Create a `.env` file and add your API credentials:

```env
ENV_NIX_APP_ID=YOUR_APP_ID
ENV_NIX_API_KEY=YOUR_API_KEY

ENV_SHEETY_ENDPOINT=YOUR_ENDPOINT
ENV_SHEETY_USERNAME=YOUR_USERNAME
ENV_SHEETY_PASSWORD=YOUR_PASSWORD
```

If using Bearer Token authentication:

```env
ENV_SHEETY_TOKEN=YOUR_TOKEN
```

---

## ▶️ How It Works

1. Enter your daily exercises in plain English.
2. Nutritionix analyzes the workout.
3. Python extracts:
   - Exercise Name
   - Duration
   - Calories Burned
4. Current date and time are generated automatically.
5. The data is sent to Google Sheets through the API.

---

## 📚 Concepts Learned

- Working with REST APIs
- Sending HTTP POST requests
- Parsing JSON responses
- API Authentication
- Environment Variables
- Google Sheets Automation
- Python Automation
- Datetime Module

---

## 🎯 Learning Outcome

By completing this project, I learned how to integrate multiple APIs into a single Python application, securely manage sensitive credentials, process JSON data, and automate the storage of workout information in Google Sheets.

---
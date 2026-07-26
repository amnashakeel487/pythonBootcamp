# 🛰️ Day 33 – API Integration & ISS Overhead Notifier

## 📌 Project Overview

Day 33 focused on learning how to work with **Application Programming Interfaces (APIs)** in Python. Throughout the day, I practiced making HTTP requests, reading JSON responses, updating a GUI with live API data, and finally built an automation project that sends an email notification when the International Space Station (ISS) is overhead at night.

---

## 📚 What I Learned

- What an API is and how it works.
- How to send HTTP GET requests using the `requests` library.
- How to work with REST APIs.
- Understanding JSON data.
- Converting JSON responses into Python dictionaries.
- Extracting nested data from JSON.
- Sending query parameters with API requests.
- Using `response.raise_for_status()` for error handling.
- Updating Tkinter GUI using live API data.
- Combining multiple APIs in one project.
- Using `datetime` to work with time.
- Automating tasks using Python.
- Sending emails using SMTP.

---

## 🛠 Projects Completed

### 1. ISS Location Tracker
- Connected to the Open Notify ISS API.
- Retrieved the current latitude and longitude of the International Space Station.
- Displayed the live coordinates in the console.

### 2. Sunrise & Sunset API
- Connected to the Sunrise-Sunset API.
- Retrieved sunrise and sunset times based on latitude and longitude.
- Extracted the hour from ISO datetime strings.

### 3. Kanye Quotes App
- Built a Tkinter GUI.
- Connected to the Kanye REST API.
- Displayed a random Kanye West quote.
- Updated the quote each time the image button was clicked.

### 4. ISS Overhead Notifier (Final Project)
- Combined multiple APIs.
- Checked the ISS live location.
- Compared ISS coordinates with my location.
- Checked whether it was currently nighttime.
- Automatically sent an email notification when the ISS was overhead.

---

## 📁 Project Structure

```text
day33/
│
├── iss_overhead/
│   └── main.py
│
├── sunrise_sunset/
│   └── main.py
│
├── kanye_quotes/
│   ├── main.py
│   ├── background.png
│   └── kanye.png
│
└── iss_overhead_notifier/
    └── main.py
```

---

## 🧰 Technologies Used

- Python
- Requests
- Tkinter
- JSON
- Datetime
- SMTP
- REST APIs

---

## 🌐 APIs Used

- Open Notify ISS API
- Sunrise-Sunset API
- Kanye REST API

---

## 💡 Key Concepts Practiced

- API Requests
- HTTP GET Method
- JSON Parsing
- Dictionary Operations
- Query Parameters
- Exception Handling
- GUI Updates
- Time & Date Handling
- Email Automation
- Python Automation Scripts

---

## 🎯 Learning Outcome

By completing Day 33, I learned how to communicate with web APIs, process real-time data, integrate multiple APIs into one application, build interactive GUI applications, and automate notifications using Python.

---

## 🚀 Next Step

Day 34 will continue building more practical projects using APIs and real-world Python automation.

---
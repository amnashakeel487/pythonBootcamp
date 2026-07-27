# 📱 Day 35 – API Keys, Authentication, Environment Variables & Sending SMS

## 📌 Project Overview
On Day 35 of the **100 Days of Python Bootcamp**, I explored how to work with secure APIs and authentication. I learned how to protect sensitive information using environment variables, retrieve live weather data from an external API, and send notifications using the Twilio SMS API.

> **Note:** Twilio's free trial and regional availability have changed since this course was created. If SMS delivery is unavailable, the project can still be completed by understanding the concepts and replacing the SMS notification with a console message.

---

## 🚀 Projects Completed

### 1️⃣ Rain Alert Application
- Connected to the OpenWeatherMap API.
- Retrieved hourly weather forecast data.
- Checked if rain was expected in the next 12 hours.
- Displayed a notification reminding the user to carry an umbrella.

### 2️⃣ Secure API Authentication
- Stored API keys and credentials in a `.env` file.
- Loaded secrets using the `python-dotenv` package.
- Prevented sensitive information from being hardcoded in the source code.

### 3️⃣ SMS Notification (Twilio)
- Learned how SMS APIs work.
- Configured Twilio credentials.
- Prepared an automated SMS notification for weather alerts.
- Understood how authentication tokens secure API requests.

---

## 📚 Concepts Learned

- What APIs are and how they work
- Making HTTP GET requests using the `requests` library
- Reading JSON responses
- Working with API Keys
- API Authentication
- Environment Variables
- Using the `.env` file
- Protecting secret credentials
- Sending SMS with Twilio
- Error handling while working with APIs

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Python-dotenv
- Twilio
- OpenWeatherMap API

---

## 📂 Project Structure

```
day35/
│
├── weather_alert/
│   ├── main.py
│   └── .env
│
├── sms_notification/
│   ├── main.py
│   └── .env
│
└── README.md
```

---

## 📦 Installation

Install the required libraries:

```bash
pip install requests
pip install python-dotenv
pip install twilio
```

Or:

```bash
pip install requests python-dotenv twilio
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📖 Key Takeaways

- APIs allow applications to communicate and exchange data.
- Environment variables help keep API keys and passwords secure.
- Authentication ensures only authorized users can access services.
- Weather APIs can be used to build real-world automation projects.
- Third-party services like Twilio enable applications to send SMS notifications.

---

## 🎯 Outcome

By the end of Day 35, I understood how to securely interact with external APIs, protect confidential credentials, retrieve live weather information, and integrate SMS notifications into Python applications. These skills are fundamental for building secure, real-world software that communicates with online services.
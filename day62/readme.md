# ☕ Coffee & WiFi Finder

## 📌 Project Overview

**Coffee & WiFi Finder** is a responsive Flask web application developed as part of **Day 61 of the 100 Days of Python Bootcamp**.

The application allows users to browse cafés suitable for studying or remote work and submit new café information through a validated web form. Instead of using a database, all café records are stored in a **CSV file**, making this project an excellent introduction to persistent data storage before learning SQL databases.

This project combines **Flask**, **WTForms**, **Bootstrap**, and **CSV file handling** to build a complete multi-page web application.

---

# 🎯 Project Goals

The objectives of this project were to:

* Build a multi-page Flask application.
* Create forms using Flask-WTF and WTForms.
* Validate user input before processing.
* Read and write data using CSV files.
* Display dynamic café information in HTML.
* Design responsive pages with Bootstrap.

---

# ✨ Features

## 🏠 Home Page

* Welcome page introducing the application
* Simple navigation to other pages

## 📋 Café Directory

* Displays all cafés stored in the CSV file
* Dynamic HTML table generated from CSV data
* Easy-to-read ratings for coffee, WiFi, and power outlets

## ➕ Add Café

* User-friendly form built with WTForms
* Input validation for required fields and URLs
* Stores new café information in the CSV file

## 📱 Responsive Design

* Bootstrap-powered responsive layout
* Mobile-friendly forms and tables
* Clean and modern user interface

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask
* Flask-WTF
* WTForms
* CSV Module

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Jinja2 Templates

## Tools

* VS Code
* Git & GitHub
* Browser Developer Tools

---

# 📂 Project Structure

```text
day61-coffee-wifi/
│
├── main.py                 # Flask application
├── forms.py                # WTForms form definitions
├── cafe-data.csv           # Café data storage
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── cafes.html
│   └── base.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
│
├── screenshots/
│   └── project-preview.png
│
└── README.md
```

---

# 📚 What I Learned

## 1. Flask-WTF & WTForms

* Creating reusable forms
* Built-in validation
* Secure form submission

## 2. HTTP Form Handling

* GET requests
* POST requests
* Processing submitted form data

## 3. CSV File Handling

* Reading CSV files
* Appending new records
* Displaying stored data dynamically

## 4. Bootstrap Integration

* Responsive forms
* Styled tables
* Navigation components
* Mobile-friendly layouts

## 5. Flask Templates

* Rendering dynamic pages
* Passing data to Jinja templates
* Organizing reusable templates

---

# 🚀 Future Improvements

Potential enhancements include:

* Replace CSV with SQLite or PostgreSQL
* Add search and filtering
* Edit and delete café entries
* User authentication
* Interactive map integration
* Image uploads for cafés

---

# 👩‍💻 Author

**Amna Shakeel**

Software Engineering Student
100 Days of Python Bootcamp Journey

---

# ⭐ Acknowledgement

This project was completed during **Day 61 of the 100 Days of Python Bootcamp**, focusing on building interactive Flask applications using WTForms, Bootstrap, and CSV-based data management.

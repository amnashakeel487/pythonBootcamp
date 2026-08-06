# ☕ Coffee & WiFi Finder

## 📌 Project Overview

This project was developed as part of **Day 62 of the 100 Days of Python Bootcamp**.

The application allows users to browse cafés that are suitable for studying or remote work and submit new café information through a validated form. Instead of using a database, the project stores café records in a **CSV file**, providing an introduction to persistent data storage before working with SQL databases.

This project combines **Flask**, **Flask-WTF**, **Bootstrap**, and **CSV file handling** to build a complete multi-page web application.

---

# 🎯 Project Goals

The objectives of this project were to:

* Build a complete Flask web application.
* Create validated forms using Flask-WTF.
* Read and write data to CSV files.
* Display café information dynamically.
* Build responsive pages using Bootstrap.
* Practice organizing a multi-page Flask project.

---

# ✨ Features

## 🏠 Home Page

* Welcome page
* Navigation between pages

## 📋 Café Directory

* Dynamic table of cafés
* Displays location, opening hours, coffee quality, WiFi strength, and power outlet ratings

## ➕ Add Café

* WTForms-powered submission form
* Validation for required fields and URLs
* Automatically saves new cafés to the CSV file

## 📱 Responsive Design

* Bootstrap-based layout
* Mobile-friendly interface
* Clean and modern design

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

---

# 📂 Project Structure

```text
day62-coffee-wifi/
│
├── main.py
├── forms.py
├── cafe-data.csv
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── cafes.html
│   └── base.html
│
├── static/
│   └── css/
│       └── styles.css
│
├── screenshots/
│   └── project-preview.png
│
└── README.md
```

---

# 📚 What I Learned

* Working with Flask-WTF in real applications
* Reading and writing CSV files
* Processing validated form data
* Rendering dynamic data with Jinja2
* Building responsive interfaces using Bootstrap
* Structuring multi-page Flask applications

---

# 🚀 Future Improvements

* Replace CSV with SQLite or PostgreSQL
* Add edit and delete functionality
* Implement search and filtering
* Add authentication for managing cafés
* Deploy the application online

---

# 👩‍💻 Author

**Amna Shakeel**

Software Engineering Student
100 Days of Python Bootcamp Journey

---

# ⭐ Acknowledgement

This project was completed during **Day 62 of the 100 Days of Python Bootcamp**, combining Flask, WTForms, Bootstrap, and CSV file handling to create a practical data-driven web application.

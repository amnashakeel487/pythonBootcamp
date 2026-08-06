# 📚 Virtual Bookshelf - Flask Database Application

![Project Preview](screenshots/project-preview.png)

## 📌 Project Overview

This project was completed as part of **Day 63 of the 100 Days of Python Bootcamp**, focusing on working with **SQLite databases** and **SQLAlchemy ORM** in Flask.

The application is a simple **Virtual Bookshelf** where users can store, view, update, and delete books. Instead of saving data in CSV files, the project uses a **SQLite database** to provide persistent storage and demonstrates how Flask applications interact with relational databases.

This project introduces **CRUD operations** and database modeling, two fundamental concepts in modern web development.

---

# 🎯 Project Goals

The objectives of this project were to:

* Learn how relational databases work.
* Connect Flask applications with SQLite.
* Use SQLAlchemy ORM to manage database operations.
* Design database models using Python classes.
* Implement Create, Read, Update, and Delete (CRUD) functionality.
* Build a data-driven Flask application.

---

# ✨ Features

## 📚 Book Collection

* View all stored books
* Display title, author, and rating
* Dynamic data loaded from the SQLite database

## ➕ Add Books

* Add new books using a form
* Store data permanently in the database

## ✏️ Update Ratings

* Modify book ratings
* Save changes directly to the database

## 🗑️ Delete Books

* Remove books from the collection
* Automatically update the displayed list

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* SQLAlchemy ORM
* SQLite

## Frontend

* HTML5
* CSS3
* Bootstrap
* Jinja2 Templates

## Tools

* VS Code
* Git & GitHub
* SQLite Viewer

---

# 📂 Project Structure

```text
day63-books-database/
│
├── main.py                 # Flask application
├── instance/
│   └── books.db            # SQLite database
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
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

## 1. SQLite Database

* Creating a local relational database
* Storing persistent application data
* Understanding tables and records

## 2. SQLAlchemy ORM

* Creating models with Python classes
* Mapping objects to database tables
* Querying data without writing raw SQL

## 3. CRUD Operations

* Create new records
* Read data from the database
* Update existing records
* Delete records safely

## 4. Flask Database Integration

* Connecting Flask to SQLite
* Managing database sessions
* Rendering database content with Jinja templates

---

# 🚀 Future Improvements

Potential enhancements include:

* Search books by title or author
* Add book cover images
* Implement user authentication
* Add categories and genres
* Replace SQLite with PostgreSQL or MySQL
* Deploy the application to the cloud

---

# 👩‍💻 Author

**Amna Shakeel**

Software Engineering Student
100 Days of Python Bootcamp Journey

---

# ⭐ Acknowledgement

This project was completed during **Day 63 of the 100 Days of Python Bootcamp**, introducing database management with SQLite and SQLAlchemy while building a complete CRUD-based Flask web application.

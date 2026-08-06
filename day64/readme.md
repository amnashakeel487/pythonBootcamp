# 🎬 My Top 10 Movies - Flask Database Application

![Project Preview](screenshots/project-preview.png)

## 📌 Project Overview

**My Top 10 Movies** is a web application developed as part of **Day 64 of the 100 Days of Python Bootcamp**.

The application allows users to create and manage their personal movie ranking list. Movies are stored permanently using a **SQLite database** and managed through **SQLAlchemy ORM**.

This project builds upon previous database concepts by implementing a complete CRUD-based application where users can add, update, view, and delete movie records.

---

# 🎯 Project Goals

The main objectives of this project were:

* Build a database-driven Flask application.
* Store movie information using SQLite.
* Manage database operations using SQLAlchemy.
* Implement CRUD functionality.
* Create dynamic pages using Jinja templates.
* Design a responsive interface using Bootstrap.

---

# ✨ Features

## 🎥 Movie Collection

* Display all saved movies
* Show movie title, year, rating, and review
* Dynamic data loaded from database

## ➕ Add Movies

* Add new movies to the collection
* Store movie details permanently

## ⭐ Rating System

* Add personal ratings
* Write reviews
* Rank favorite movies

## ✏️ Edit Movies

* Update movie information
* Modify ratings and reviews

## 🗑️ Delete Movies

* Remove movies from collection
* Update database records

## 📱 Responsive Design

* Bootstrap-based UI
* Clean movie card layout
* Mobile-friendly interface

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
* Bootstrap 5
* Jinja2 Templates

## Tools

* VS Code
* Git & GitHub
* SQLite Viewer

---

# 📂 Project Structure

```text
day64-top-movies/
│
├── main.py                 # Flask application
│
├── instance/
│   └── movies.db           # SQLite database
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── delete.html
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

## 1. Database Integration

* Connecting Flask with SQLite
* Creating database models
* Managing persistent data

## 2. SQLAlchemy ORM

* Creating tables using Python classes
* Querying database records
* Updating and deleting records

## 3. CRUD Operations

Implemented:

* Create movie records
* Read movie information
* Update movie details
* Delete movies

## 4. Flask Application Structure

Learned how to organize:

* Routes
* Templates
* Static files
* Database models

## 5. Bootstrap UI Design

Improved frontend skills by creating:

* Responsive layouts
* Cards
* Buttons
* Clean user interfaces

---

# 🚀 Future Improvements

Possible enhancements:

* User accounts and authentication
* Search movies
* Add movie posters using APIs
* Connect with TMDB API
* Add categories and genres
* Deploy online

---

# 👩‍💻 Author

**Amna Shakeel**

Software Engineering Student
100 Days of Python Bootcamp Journey

---

# ⭐ Acknowledgement

This project was completed during **Day 64 of the 100 Days of Python Bootcamp**, where I learned how to build database-driven Flask applications using SQLite, SQLAlchemy ORM, and Bootstrap.

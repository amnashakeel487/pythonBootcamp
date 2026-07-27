# 🧠 Quizzler App – Day 34

A desktop-based Quiz Application developed in **Python** using **Tkinter**, **Object-Oriented Programming (OOP)**, and the **Open Trivia Database API**. The application retrieves live True/False questions from an online API, presents them through an interactive graphical interface, tracks the user's score, and provides immediate feedback after each response.

This project demonstrates how to integrate external APIs into a desktop application while maintaining a clean, modular, and scalable code structure.

---

## 📖 Project Overview

The Quizzler App connects to the Open Trivia Database API to fetch trivia questions dynamically. Questions are displayed one at a time, allowing users to answer using True or False buttons. The application validates each response, updates the score, provides visual feedback, and displays the final result after all questions have been completed.

---

## ✨ Features

- Retrieve live trivia questions from the Open Trivia API
- Interactive graphical user interface built with Tkinter
- True/False answer selection
- Real-time score tracking
- Instant visual feedback for correct and incorrect answers
- Automatic loading of the next question
- End-of-quiz completion message
- Modular project structure using Object-Oriented Programming

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Requests Library
- HTML Module
- Open Trivia Database (OpenTDB) API

---

## 📂 Project Structure

```
day34/
│
├── main.py               # Entry point of the application
├── data.py               # Retrieves quiz questions from the API
├── question_model.py     # Question class
├── quiz_brain.py         # Quiz logic and score management
├── ui.py                 # Graphical User Interface
├── images/
│   ├── true.png
│   └── false.png
└── README.md
```

---

## 🎯 Learning Objectives

During this project, the following concepts were practiced:

- Consuming REST APIs
- Sending API query parameters
- Parsing JSON responses
- Object-Oriented Programming (Classes & Objects)
- Separating application logic into multiple modules
- Building desktop applications with Tkinter
- Using Canvas, Labels, Buttons, and Images
- Event handling in GUI applications
- Scheduling tasks with the `after()` method
- Decoding HTML entities using the `html` module

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd day34
```

### 3. Install the required package

```bash
pip install requests
```

### 4. Run the application

```bash
python main.py
```

---

## 📸 Application Workflow

1. The application requests quiz questions from the Open Trivia Database API.
2. Questions are converted into Question objects.
3. The QuizBrain class manages quiz progression and scoring.
4. The Tkinter interface displays each question.
5. Users answer using the **True** or **False** buttons.
6. The application immediately indicates whether the answer is correct.
7. The score updates after every question.
8. A completion message is displayed once the quiz ends.

---

## 📚 Key Python Concepts Covered

- API Integration
- HTTP Requests
- JSON Data Handling
- Object-Oriented Programming
- Tkinter GUI Development
- Event-Driven Programming
- Module Organization
- Error-Free User Interface Updates

---

## 💡 Skills Gained

After completing this project, you will be able to:

- Build interactive desktop GUI applications
- Integrate third-party REST APIs into Python projects
- Work with JSON data from web services
- Design modular applications using Object-Oriented Programming
- Handle user interactions through graphical interfaces
- Develop clean, maintainable, and reusable Python code

---

## 📈 Future Improvements

Possible enhancements include:

- Multiple quiz categories
- Difficulty level selection
- Timer for each question
- High score tracking
- User profiles
- Sound effects and animations
- Dark mode interface

---

## 🏁 Conclusion

The **Quizzler App** is a practical project that combines **API integration**, **GUI development**, and **Object-Oriented Programming** into a complete desktop application. It strengthens the understanding of real-world software architecture while demonstrating how external data sources can be incorporated into interactive Python applications.
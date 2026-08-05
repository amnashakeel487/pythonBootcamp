# 🎮 Higher Lower Game using Flask

## Overview

This project is a simple web-based guessing game built with Flask. The application generates a random number between 0 and 9, and users try to guess it by entering a number directly into the browser URL.

## Features

- Flask web server
- Dynamic URL routing
- Random number generation
- Too High / Too Low feedback
- Success page when the correct number is guessed
- HTML responses with images and colors

## Technologies Used

- Python
- Flask

## Project Structure

```
day55/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
pip install Flask
```

## Run

```bash
python main.py
```

Open:

```
http://127.0.0.1:5000
```

Guess by visiting:

```
http://127.0.0.1:5000/5
```

Replace **5** with your own guess.

## Learning Outcomes

- Flask Routing
- Dynamic URL Variables
- URL Parsing
- HTML Responses
- Random Number Generation
- Conditional Logic
- Building Interactive Web Applications
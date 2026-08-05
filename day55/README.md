# 🎮 Higher Lower Game using Flask

## Overview

This project is a simple web-based guessing game built with Flask. The application generates a random number between 0 and 9, and users try to guess it by entering a number directly into the browser URL.

<img width="1407" height="977" alt="image" src="https://github.com/user-attachments/assets/c0cd7b2a-1f6e-4603-961d-081eb1f431ed" />
<img width="1365" height="1031" alt="image" src="https://github.com/user-attachments/assets/18b3402f-c00d-4df4-8c12-c704a91d37d4" />


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

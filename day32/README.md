# Day 32 - Email Automation with SMTP & Datetime

## Project Overview

On **Day 32** of the 100 Days of Python Bootcamp, I learned how to automate email sending using Python. This project introduced the **SMTP protocol**, the **datetime module**, and email automation by building three practical applications:

- Sending an email using Python
- Monday Motivation Email Sender
- Automatic Birthday Wisher

These projects demonstrate how Python can automate repetitive tasks by combining networking, file handling, dates, randomness, and CSV data.

---

## Projects Completed

### 1. Send an Email

- Connected to Gmail's SMTP server
- Logged into a Gmail account using an App Password
- Sent a custom email using Python

### 2. Sunday Motivation

- Checked the current day using the `datetime` module
- Read motivational quotes from a text file
- Selected a random quote
- Automatically emailed the quote every Monday

### 3. Birthday Wisher

- Read birthday information from a CSV file using Pandas
- Checked if today's date matched any birthday
- Selected a random birthday letter template
- Replaced the recipient's name dynamically
- Automatically sent a personalized birthday email

---

## Technologies Used

- Python 3
- SMTP (Simple Mail Transfer Protocol)
- smtplib
- datetime
- Pandas
- CSV Files
- Random Module
- File Handling

---

## Project Structure

```
day32/
│
├── send_an_email/
│   └── main.py
│
├── sunday_motivation/
│   ├── main.py
│   └── quotes.txt
│
├── birthday_wisher/
│   ├── main.py
│   ├── birthdays.csv
│   └── letter_templates/
│       ├── letter_1.txt
│       ├── letter_2.txt
│       └── letter_3.txt
│
└── README.md
```

---

## Concepts Practiced

- SMTP Protocol
- Email Automation
- Gmail SMTP Server
- App Password Authentication
- datetime Module
- Current Date & Time
- Weekday Detection
- Pandas DataFrames
- Reading CSV Files
- Dictionary Comprehension
- File Handling
- Random Module
- String Replacement
- Python Automation

---

## Learning Outcomes

After completing Day 32, I can:

- Send emails using Python.
- Connect securely to Gmail's SMTP server.
- Use App Passwords for email authentication.
- Work with dates and times using the `datetime` module.
- Read and process CSV files with Pandas.
- Automate emails based on specific dates.
- Generate personalized emails using templates.
- Build real-world Python automation projects.

---

## How to Run

1. Install Python 3.

2. Install Pandas:

```bash
pip install pandas
```

3. Replace the following in the code:

```
MY_EMAIL
APP_PASSWORD
```

with your own Gmail address and Google App Password.

4. Run any project:

```bash
python main.py
```

---

## Future Improvements

- Support HTML email formatting.
- Send emails with file attachments.
- Schedule emails automatically.
- Add logging for sent emails.
- Support multiple email providers.
- Build a graphical interface for email management.

---

## Author

**Amna Shakeel**

100 Days of Python Bootcamp – Day 32
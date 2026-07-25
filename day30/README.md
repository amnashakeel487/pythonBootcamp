# Day 30 - Improved Password Manager (JSON Data Storage)

## Project Overview

On **Day 30** of the 100 Days of Python Bootcamp, I enhanced the Password Manager created on Day 29 by replacing the text file storage with **JSON** and adding a **Search** feature. This made the application more organized, efficient, and similar to how real-world applications store and retrieve data.

The project focuses on working with JSON files, exception handling, and improving an existing application instead of building one from scratch.

---

# Improvements from Day 29

### Day 29

- Stored passwords in a plain text file (`data.txt`)
- Generated secure random passwords
- Saved website, email, and password
- Used Tkinter GUI
- Copied generated passwords to the clipboard

### Day 30

- Replaced `data.txt` with `data.json`
- Stored credentials in a structured JSON format
- Added a **Search** button to find saved credentials
- Updated existing data without deleting previous records
- Used exception handling to prevent crashes
- Automatically created the JSON file if it did not exist
- Improved the application's reliability and usability

---

# Features

- Graphical User Interface (Tkinter)
- Generate strong random passwords
- Automatically copy password to clipboard
- Save credentials in JSON format
- Search saved credentials by website
- Update existing password records
- Confirmation dialog before saving
- Input validation
- Exception handling
- Automatically create JSON file if missing

---

# Technologies Used

- Python 3
- Tkinter
- JSON Module
- Random Module
- Messagebox
- File Handling
- Exception Handling

---

# Project Files

```
day30/
│── main.py
│── logo.png
│── data.json
└── README.md
```

---

# How It Works

### Saving Data

1. Enter the website name.
2. Enter your email or username.
3. Generate a secure password (optional).
4. Click **Add**.
5. Confirm the details.
6. Credentials are saved inside `data.json`.

### Searching Data

1. Enter the website name.
2. Click **Search**.
3. If the website exists, the saved email and password are displayed.
4. If it doesn't exist, an error message is shown.

---

# Example JSON Data

```json
{
    "Google": {
        "email": "your_email@example.com",
        "password": "A8#gP2!Lm9"
    },
    "GitHub": {
        "email": "your_email@example.com",
        "password": "Qw9@Rt5!Xz"
    }
}
```

---

# Concepts Practiced

- JSON File Handling
- `json.dump()`
- `json.load()`
- Dictionary Operations
- Nested Dictionaries
- `dictionary.update()`
- Exception Handling
- `try`
- `except FileNotFoundError`
- `messagebox.showinfo()`
- Tkinter GUI Development
- Random Password Generation
- Clipboard Operations
- Input Validation

---

# Exception Handling Used

### FileNotFoundError

Creates a new JSON file if it does not already exist.

### JSON Data Reading

Safely reads existing data before updating it.

### Updating Existing Data

New credentials are added without removing previously saved passwords.

---

# How to Run

1. Install Python 3.
2. Place these files in the same folder:

```
main.py
logo.png
```

> **Note:** `data.json` will be created automatically the first time you save a password if it does not already exist.

3. Open a terminal or command prompt.

4. Run the application:

```bash
python main.py
```

---

# Learning Outcomes

After completing this project, I can:

- Work with JSON files in Python.
- Read and write structured data using the `json` module.
- Update existing JSON data without overwriting it.
- Handle file-related exceptions gracefully.
- Search for specific records inside a JSON file.
- Improve an existing application by adding new functionality.
- Build more robust desktop applications using Tkinter.

---

# Future Improvements

- Encrypt stored passwords for better security.
- Add a Delete Password feature.
- Add an Edit/Update Password option.
- Save passwords in an encrypted database.
- Add a password strength indicator.
- Implement user authentication before accessing saved passwords.

---

# Author

**Amna Shakeel**

100 Days of Python Bootcamp – Day 30
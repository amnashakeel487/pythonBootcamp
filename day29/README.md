# Day 29 - Password Manager

## Project Overview

On Day 29 of the 100 Days of Python Bootcamp, I built a **Password Manager** using Python's Tkinter library. This desktop application allows users to generate strong random passwords, store login credentials, and save them in a local text file for future use.

The project combines GUI development, password generation, file handling, clipboard operations, and user input validation into one practical application.

---

<img width="1425" height="935" alt="1" src="https://github.com/user-attachments/assets/6c49a184-6b59-497e-a161-099508f781ed" />
<img width="1462" height="902" alt="2" src="https://github.com/user-attachments/assets/3819465d-b628-4ae0-8eb0-b20afea5a6f0" />
<img width="1280" height="851" alt="3" src="https://github.com/user-attachments/assets/70b6d28d-7fa0-450d-8499-532683aad6f6" />


## Features

- User-friendly graphical interface
- Generate strong random passwords
- Automatically fills the password field
- Copies generated password to clipboard
- Save website, email, and password
- Confirmation dialog before saving
- Input validation for empty fields
- Automatically clears fields after saving
- Focus returns to the Website field for faster entry

---

## Technologies Used

- Python 3
- Tkinter (GUI Library)
- Random Module
- Tkinter Messagebox
- File Handling

---

## Project Files

```
day29/
│── main.py
│── logo.png
│── data.txt
└── README.md
```

---

## How It Works

1. Enter the website name.
2. Enter your email or username.
3. Click **Generate Password** to create a secure password.
4. The generated password is automatically copied to the clipboard.
5. Click **Add**.
6. Confirm the details in the popup dialog.
7. The credentials are saved in `data.txt`.

---

## Example Saved Data

```
Google | your_email@example.com | A8#gP2!Lm9
GitHub | your_email@example.com | k#3Lp9@Qw1
Amazon | your_email@example.com | Zx8$Rt2!Mn
```

---

## Concepts Practiced

- Tkinter GUI Development
- Labels
- Entry Widgets
- Buttons
- Canvas
- Images using PhotoImage
- Grid Layout
- Event Handling
- Random Password Generation
- List Comprehensions
- Random Module
- File Handling
- Clipboard Operations
- Input Validation
- Message Boxes
- Functions

---

## How to Run

1. Install Python 3.
2. Place the following files in the same folder:

```
main.py
logo.png
data.txt
```

3. Open a terminal or command prompt.

4. Run:

```bash
python main.py
```

---

## Learning Outcomes

After completing this project, I can:

- Build GUI applications with Tkinter.
- Generate secure random passwords.
- Validate user input.
- Save data to text files.
- Display confirmation and warning dialogs.
- Use clipboard functionality.
- Organize Python applications into reusable functions.

---

## Future Improvements

- Save passwords using JSON instead of plain text.
- Search saved passwords by website.
- Update existing passwords.
- Delete saved credentials.
- Encrypt stored passwords for improved security.

---

## Author

**Amna Shakeel**

100 Days of Python Bootcamp

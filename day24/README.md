# 📧 Mail Merge Challenge

A simple Python application that automatically generates personalized letters using a template and a list of recipient names. This project demonstrates Python file handling, string manipulation, and file automation.

Developed as part of **Day 24** of the **100 Days of Python Bootcamp**.

---

## 📌 Features

- 📄 Reads a letter template from a text file.
- 👥 Reads a list of names from a separate file.
- ✏️ Replaces the placeholder (`[name]`) with each person's name.
- 📁 Automatically creates a personalized letter for every recipient.
- 🏗️ Uses relative file paths for better project organization.
- 📂 Saves all generated letters in a separate output folder.

---

## 📂 Project Structure

```
Mail Merge Project/
│
├── main.py
│
├── Input/
│   ├── Letters/
│   │     └── starting_letter.txt
│   │
│   └── Names/
│         └── invited_names.txt
│
└── Output/
    └── ReadyToSend/
```

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

---

## 🎯 How It Works

1. Reads all names from **invited_names.txt**.
2. Reads the template from **starting_letter.txt**.
3. Replaces the placeholder **[name]** with each recipient's name.
4. Creates a new personalized text file for every name.
5. Saves all generated letters inside the **Output/ReadyToSend** folder.

---

## 📄 Example Input

### starting_letter.txt

```
Dear [name],

You are invited to my birthday party.

Hope to see you there!

Regards,
Amna
```

### invited_names.txt

```
Ali
Ahmed
Sara
Fatima
```

---

## 📄 Example Output

The program automatically creates:

```
Output/
└── ReadyToSend/
    ├── letter_for_Ali.txt
    ├── letter_for_Ahmed.txt
    ├── letter_for_Sara.txt
    └── letter_for_Fatima.txt
```

Each file contains a personalized version of the original letter.

---

## 💻 Technologies Used

- Python
- File Handling
- String Manipulation

---

## 📚 Python Concepts Practiced

- File Handling
- `with open()`
- Reading Files (`read()`, `readlines()`)
- Writing Files (`write()`)
- Relative File Paths
- String Methods (`replace()`, `strip()`)
- Loops
- Variables
- f-Strings
- File Automation

---

## 🎓 Learning Outcomes

After completing this project, you will understand how to:

- Read data from text files.
- Write data to new files.
- Use the `with` statement for safe file handling.
- Work with relative file paths.
- Replace text using Python string methods.
- Generate multiple personalized files automatically.
- Organize files into a structured project.

---

## 🌟 Project Highlights

- Beginner-friendly project.
- Demonstrates real-world file automation.
- Shows how one template can generate many personalized documents.
- Reinforces file handling and string manipulation concepts.

---

## 👨‍💻 Author

Developed as part of the **100 Days of Python Bootcamp** to practice Python file handling, automation, and text processing.

---

⭐ This project demonstrates how Python can automate repetitive tasks by generating personalized documents from a single template.
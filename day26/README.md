# Day 26 - Working with List & Dictionary Comprehensions | NATO Phonetic Alphabet Project

## 📖 Overview

Day 26 focused on mastering **List Comprehension** and **Dictionary Comprehension**, two powerful Python features that allow writing shorter, cleaner, and more efficient code.

The day began by practicing list and dictionary comprehensions through multiple exercises, including finding common numbers between two files, calculating word lengths, and converting temperatures from Celsius to Fahrenheit.

Finally, these concepts were applied in a real-world project by building a **NATO Phonetic Alphabet Converter**, which reads data from a CSV file using Pandas and converts any user-entered word into its corresponding NATO phonetic alphabet.

---

# Topics Covered

## 1. List Comprehension

- Creating lists in a single line
- Using loops inside list comprehensions
- Applying conditions
- Reading files and creating lists
- Finding common elements between two files

Example:

```python
numbers = [1, 2, 3, 4, 5]

square_numbers = [number ** 2 for number in numbers]
```

---

## 2. Dictionary Comprehension

- Creating dictionaries in one line
- Iterating through dictionaries
- Using `.items()`
- Applying conditions
- Transforming dictionary values

Example:

```python
student_scores = {
    "Ali": 85,
    "Sara": 72,
    "Ahmed": 93
}

passed_students = {
    student: score
    for (student, score) in student_scores.items()
    if score >= 80
}
```

---

## 3. Working with CSV Files

- Reading CSV files
- Using Pandas
- Creating DataFrames
- Accessing rows and columns
- Converting DataFrame data into dictionaries

Example:

```python
import pandas as pd

data = pd.read_csv("file.csv")
```

---

## 4. Pandas DataFrames

Learned how to:

- Read CSV files
- Access columns
- Iterate through rows
- Use `iterrows()`
- Convert DataFrame into Dictionary

---

## 5. Exception Handling

Used:

- try
- except
- KeyError

to prevent program crashes when invalid characters are entered.

---

# Exercises Completed

### Exercise 1
Finding common numbers from two text files using List Comprehension.

### Exercise 2
Creating a dictionary containing the length of every word in a sentence using Dictionary Comprehension.

### Exercise 3
Converting Celsius temperatures into Fahrenheit using Dictionary Comprehension.

---

# Main Project

# NATO Phonetic Alphabet Converter

## Description

Built a command-line application that converts any English word into its corresponding NATO phonetic alphabet.
Example:


<img width="707" height="386" alt="1" src="https://github.com/user-attachments/assets/9827200f-93b3-455c-ab4b-74f84f34a856" />


The project reads NATO alphabet data from a CSV file using the Pandas library and converts it into a dictionary using Dictionary Comprehension.

The user enters a word, and the program translates every letter using List Comprehension.

If invalid characters are entered, the program displays an error message and asks the user to try again.

---

# Features

- Read CSV files using Pandas
- Convert DataFrame into Dictionary
- Dictionary Comprehension
- List Comprehension
- User Input
- Input Validation
- Exception Handling
- Unlimited conversions until user exits

---

# Concepts Used

- Python Functions
- Loops
- Lists
- Dictionaries
- List Comprehension
- Dictionary Comprehension
- Pandas Library
- CSV File Handling
- DataFrames
- iterrows()
- User Input
- try-except
- KeyError

---

# Requirements

Python 3.x

Install Pandas

```bash
pip install pandas
```

---

# How to Run

1. Open the project folder.

2. Install Pandas.

3. Ensure the following files are present:

```
main.py
nato_phonetic_alphabet.csv
```

---

# Learning Outcomes

After completing Day 26, I learned how to:

- Write cleaner code using List Comprehension.
- Create dictionaries efficiently using Dictionary Comprehension.
- Read and process CSV files using Pandas.
- Work with DataFrames and iterate through rows.
- Convert DataFrame data into Python dictionaries.
- Build a practical command-line application.
- Handle invalid user input using exception handling.
- Improve code readability and efficiency with Python comprehensions.

---

# Technologies Used

- Python 3
- Pandas
- CSV Files

---

# Author

**Amna Shakeel**

Completed as part of the **100 Days of Python Bootcamp – Day 26**.

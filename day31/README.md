# Day 31 - Flash Card App

## Project Overview

On **Day 31** of the 100 Days of Python Bootcamp, I built a **Flash Card Application** using Python, Tkinter, and Pandas. The application helps users learn French vocabulary by displaying a French word and automatically flipping the card after a few seconds to reveal its English translation.

The app also tracks learning progress by removing words the user already knows and saving the remaining words in a separate CSV file.

---

<img width="1121" height="946" alt="1" src="https://github.com/user-attachments/assets/8560a3cc-e77b-478e-8a9a-474929d3cf70" />
<img width="1127" height="947" alt="2" src="https://github.com/user-attachments/assets/791f2d29-f03d-4de6-b393-4ddea2b82135" />

## Features

- Display random French vocabulary.
- Automatically flip the flash card after 3 seconds.
- Show the English translation.
- Mark known words using the ✔ button.
- Skip unknown words using the ✖ button.
- Save learning progress automatically.
- Resume learning from where you left off.
- Clean and interactive graphical user interface.

---

## Technologies Used

- Python 3
- Tkinter
- Pandas
- CSV Files
- Random Module

---

## Project Structure

```
day31/
│
├── main.py
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── README.md
```

---

## How It Works

1. Load French vocabulary from the CSV file.
2. Display a random French word.
3. Wait for 3 seconds.
4. Flip the flash card to show the English translation.
5. Click:
   - ✔ if you know the word.
   - ✖ if you don't know the word.
6. Known words are removed from the learning list.
7. Remaining words are saved in `words_to_learn.csv`.

---

## Concepts Practiced

- Tkinter GUI
- Canvas Widget
- Working with Images
- Pandas DataFrames
- CSV File Handling
- Dictionaries
- Random Module
- Timers using `after()`
- Canceling Timers using `after_cancel()`
- Exception Handling
- Data Persistence

---

## Learning Outcomes

After completing this project, I can:

- Build interactive desktop applications using Tkinter.
- Read and write CSV files using Pandas.
- Convert DataFrames into dictionaries.
- Display images and text on a Canvas.
- Create timers with `after()`.
- Update GUI elements dynamically.
- Save user progress between sessions.
- Build a complete capstone project using multiple Python concepts.

---

## Future Improvements

- Support multiple languages.
- Add pronunciation audio.
- Display learning statistics.
- Add categories (Food, Travel, Colors, etc.).
- Include dark mode.
- Add keyboard shortcuts.
- Shuffle words intelligently based on difficulty.

---

## How to Run

1. Install Python 3.

2. Install Pandas:

```bash
pip install pandas
```

3. Keep the following folders together:

```
main.py
images/
data/
```

4. Run the application:

```bash
python main.py
```

---

## Author

**Amna Shakeel**

100 Days of Python Bootcamp – Day 31

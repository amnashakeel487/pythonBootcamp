# 🐢 Turtle Crossing Game (Day 23)

A fun arcade-style game built using **Python**, **Object-Oriented Programming (OOP)**, and the **Turtle Graphics** library. The objective is to help the turtle safely cross the road while avoiding moving cars. Each successful crossing increases the level and makes the game more challenging by speeding up the cars.

This project was developed as part of **Day 23** of the **100 Days of Python Bootcamp**.

---

## 📌 Features

- 🐢 Control the turtle using the keyboard.
- 🚗 Randomly generated cars with different colors.
- ⚡ Cars increase in speed after each completed level.
- 📈 Level tracking and display.
- 💥 Collision detection with cars.
- 🔄 Player resets to the starting position after reaching the finish line.
- ❌ Game Over message when the turtle is hit.
- 🏗️ Modular design using Object-Oriented Programming.

---

## 📂 Project Structure

```
day23/
│
├── main.py          # Main game loop
├── player.py        # Player (turtle) class
├── car_manager.py   # Car creation and movement
├── scoreboard.py    # Level display and Game Over
└── README.md
```

---

## 🛠️ Requirements

- Python 3.x
- Turtle Graphics (Built into Python)
- time module
- random module

No external libraries are required.

---


## 🎮 How to Play

### Controls

| Key | Action |
|------|--------|
| ↑ Up Arrow | Move the turtle forward |

---

## 🎯 Objective

- Help the turtle safely cross the road.
- Avoid all moving cars.
- Reach the finish line to advance to the next level.
- Every new level increases the speed of the cars.
- The game ends if a car hits the turtle.

---

## 🏆 Game Rules

- The turtle starts at the bottom of the screen.
- Cars continuously move from right to left.
- New cars appear randomly.
- Each successful crossing increases the level.
- Car speed increases after every level.
- If the turtle collides with any car, the game ends.

---

## 💻 Technologies Used

- Python
- Turtle Graphics
- Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Used

- Classes and Objects
- Inheritance
- Constructors (`__init__`)
- Methods
- Attributes
- Encapsulation
- Multiple Object Instances
- Modular Programming

---


## 📷 Game Preview

The game includes:

- 🐢 Turtle player
- 🚗 Random moving cars
- 📈 Level counter
- ⚡ Increasing difficulty
- 💥 Collision detection
- ❌ Game Over screen

---

## 👨‍💻 Author

Developed as part of the **100 Days of Python Bootcamp** to practice Object-Oriented Programming, Turtle Graphics, event-driven programming, and Python game development.

---

⭐ Have fun crossing the road and see how many levels you can complete!
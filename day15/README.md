
# ☕ Day 15 – Coffee Machine Management System

## 📖 Overview

Day 15 marks the beginning of the **Intermediate Level** of the **100 Days of Code: Python Bootcamp**. In this project, I built a **Coffee Machine Management System**, a console-based application that simulates the operation of a real coffee vending machine. Alongside the project, I also learned how to set up a local Python development environment using Visual Studio Code for professional software development.

---

<img width="1151" height="756" alt="1" src="https://github.com/user-attachments/assets/500036e2-b658-43fe-8594-d4eb8426b6dd" />
<img width="840" height="506" alt="2" src="https://github.com/user-attachments/assets/0a0b3f70-0810-45e0-9283-11bb82d9ced5" />


## 🎯 Objectives

* Set up a local Python development environment.
* Build a real-world console application.
* Practice organizing code into reusable functions.
* Work with nested dictionaries to manage menu items and ingredients.
* Simulate resource management and payment processing.

---

## ✨ Features

* ☕ Choose between **Espresso**, **Latte**, and **Cappuccino**
* 💧 Check if enough resources are available before preparing a drink
* 💰 Accept quarters, dimes, nickels, and pennies as payment
* 💵 Calculate the total amount inserted
* 🔄 Return change when extra money is provided
* 📊 Generate a resource and profit report
* 🧾 Track the machine's total profit
* 🚫 Display an error if resources or payment are insufficient
* 🔁 Continue serving customers until the machine is turned off
* 🔌 Shut down the machine using the **off** command

---

## 🧠 Concepts Practiced

* Python Functions
* Dictionaries
* Nested Dictionaries
* Loops (`while`)
* Conditional Statements (`if`, `elif`, `else`)
* Global Variables
* Return Values
* User Input
* Resource Management
* Payment Processing
* Modular Programming
* Local Python Development

---

## 📂 Project Structure

```text
Day15-CoffeeMachine/
│
└── main.py
│
└── menu.py
│
└── resources.py
│
└── art.py
```

## ⚙️ How the Program Works

1. The user selects a coffee (`espresso`, `latte`, or `cappuccino`).
2. The machine checks whether sufficient resources are available.
3. If resources are available, the machine asks the user to insert coins.
4. The total amount entered is calculated.
5. The machine verifies whether the payment is sufficient.
6. If payment is successful:

   * Any extra money is returned as change.
   * Resources are deducted.
   * Profit is updated.
   * The selected coffee is served.
7. The program continues serving customers until the user enters `off`.

---

## 💻 Sample Output

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is your latte ☕ Enjoy!

What would you like? (espresso/latte/cappuccino): report

Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

---

## 📚 Learning Outcomes

By completing this project, I learned how to:

* Develop larger Python applications using functions and structured logic.
* Manage application state using dictionaries and variables.
* Simulate a real-world coffee machine with resource and payment management.
* Write cleaner, modular, and reusable Python code.
* Transition from beginner projects to intermediate-level application development.

---

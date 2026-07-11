
☕ Day 15 – Coffee Machine Management System
📖 Overview

Day 15 marks the beginning of the Intermediate Level of the 100 Days of Code: Python Bootcamp. In this project, I built a Coffee Machine Management System, a console-based application that simulates the operation of a real coffee vending machine. Alongside the project, I also learned how to set up a local Python development environment using Visual Studio Code for professional software development.

<img width="1151" height="756" alt="1" src="https://github.com/user-attachments/assets/89f75600-df03-4f2a-a907-92b772bb969c" />
<img width="840" height="506" alt="2" src="https://github.com/user-attachments/assets/e531ca6e-816f-4907-a6c4-f165567928ff" />

🎯 Objectives
Set up a local Python development environment.
Build a real-world console application.
Practice organizing code into reusable functions.
Work with nested dictionaries to manage menu items and ingredients.
Simulate resource management and payment processing.
✨ Features
☕ Choose between Espresso, Latte, and Cappuccino
💧 Check if enough resources are available before preparing a drink
💰 Accept quarters, dimes, nickels, and pennies as payment
💵 Calculate the total amount inserted
🔄 Return change when extra money is provided
📊 Generate a resource and profit report
🧾 Track the machine's total profit
🚫 Display an error if resources or payment are insufficient
🔁 Continue serving customers until the machine is turned off
🔌 Shut down the machine using the off command

🧠 Concepts Practiced
Python Functions
Dictionaries
Nested Dictionaries
Loops (while)
Conditional Statements (if, elif, else)
Global Variables
Return Values
User Input
Resource Management
Payment Processing
Modular Programming
Local Python Development

📂 Project Structure
Day15-CoffeeMachine/
│
└── main.py
│
└── resource.py
│
└── menu.py
│
└── art.py


⚙️ How the Program Works
The user selects a coffee (espresso, latte, or cappuccino).
The machine checks whether sufficient resources are available.
If resources are available, the machine asks the user to insert coins.
The total amount entered is calculated.
The machine verifies whether the payment is sufficient.
If payment is successful:
Any extra money is returned as change.
Resources are deducted.
Profit is updated.
The selected coffee is served.
The program continues serving customers until the user enters off.
💻 Sample Output
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


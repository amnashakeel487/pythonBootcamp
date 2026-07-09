import os

logo = r'''
 _____________________
|  _________________  |
| | Pythonista 0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

# ---------------- FUNCTIONS ----------------

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero!"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:

        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation!")
            continue

        second_number = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(first_number, second_number)

        print(f"\n{first_number} {operation_symbol} {second_number} = {answer}")

        choice = input(
            f"\nType 'y' to continue calculating with {answer}, "
            f"'n' to start a new calculation, or 'q' to quit: "
        ).lower()

        if choice == "y":
            first_number = answer

        elif choice == "n":
            os.system("cls" if os.name == "nt" else "clear")
            calculator()
            return

        else:
            should_continue = False
            print("\nCalculator Closed.")


calculator()
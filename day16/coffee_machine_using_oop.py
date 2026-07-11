MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


class CoffeeMachine:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0

    def report(self):
        print("\n----- REPORT -----")
        print(f"Water : {self.resources['water']}ml")
        print(f"Milk  : {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money : ${self.money}")
        print("------------------")

    def check_resources(self, drink):
        ingredients = MENU[drink]["ingredients"]

        for item in ingredients:
            if self.resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False

        return True

    def process_coins(self):
        print("\nInsert Coins")

        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        total = (
            quarters * 0.25
            + dimes * 0.10
            + nickels * 0.05
            + pennies * 0.01
        )

        return total

    def make_coffee(self, drink):
        ingredients = MENU[drink]["ingredients"]

        for item in ingredients:
            self.resources[item] -= ingredients[item]

        print(f"Here is your {drink}. Enjoy! ☕")

    def start(self):

        machine_on = True

        while machine_on:

            choice = input(
                "\nWhat would you like? (espresso/latte/cappuccino): "
            ).lower()

            if choice == "off":
                machine_on = False

            elif choice == "report":
                self.report()

            elif choice in MENU:

                if self.check_resources(choice):

                    payment = self.process_coins()

                    cost = MENU[choice]["cost"]

                    if payment >= cost:

                        change = round(payment - cost, 2)

                        print(f"Here is ${change} in change.")

                        self.money += cost

                        self.make_coffee(choice)

                    else:
                        print("Sorry that's not enough money. Money refunded.")

            else:
                print("Invalid choice.")


coffee_machine = CoffeeMachine()

coffee_machine.start()
from menu import MENU
from resources import resources
from art import logo

print(logo)
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted."""
    global profit

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)

        if change > 0:
            print(f"Here is ${change} in change.")

        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct resources and serve coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕ Enjoy!")


is_on = True

while is_on:

    choice = input(
        "\nWhat would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice in MENU:

        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):

            payment = process_coins()

            if is_transaction_successful(
                payment,
                drink["cost"]
            ):
                make_coffee(
                    choice,
                    drink["ingredients"]
                )
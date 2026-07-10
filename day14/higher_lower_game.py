import random
import os

from art import logo, vs
from data import data


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def format_data(account):
    """Returns formatted account information."""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}."


def check_answer(guess, a_followers, b_followers):
    """Returns True if guess is correct."""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


print(logo)

score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
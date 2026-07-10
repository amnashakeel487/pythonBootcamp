import random

logo = r"""
 _   _                 _                 
| \ | |               | |                
|  \| |_   _ _ __ ___ | |__   ___ _ __   
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  
| |\  | |_| | | | | | | |_) |  __/ |     
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     

   _____                     _             
  / ____|                   (_)            
 | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |__| | |_| |  __/\__ \__ \ | | | | (_| |
  \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                      __/ |
                                     |___/
"""
# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check the user's guess
def check_answer(guess, answer, turns):
    """Checks the user's guess against the answer and returns the remaining turns."""

    if guess > answer:
        print("Too high.")
        return turns - 1

    elif guess < answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {answer}.")


# Function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Main Game
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != answer:

        print(f"\nYou have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if guess != answer:

            if turns == 0:
                print("You've run out of guesses. You lose.")
                print(f"The correct number was {answer}.")
                return
            else:
                print("Guess again.")


game()
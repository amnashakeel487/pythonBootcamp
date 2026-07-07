import random

# ---------------- HANGMAN TITLE ----------------

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
''')

print("Welcome to Hangman!")
print("Guess the word before you run out of lives.\n")

# ---------------- HANGMAN STAGES ----------------

stages = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

# ---------------- WORD LIST ----------------

word_list = [
    "python",
    "apple",
    "banana",
    "computer",
    "keyboard",
    "monitor",
    "program",
    "hangman",
    "internet",
    "software"
]

# ---------------- RANDOM WORD ----------------

chosen_word = random.choice(word_list)

# ---------------- CREATE BLANKS ----------------

display = []

for letter in chosen_word:
    display.append("_")

lives = 6
game_over = False
guessed_letters = []

# ---------------- GAME LOOP ----------------

while not game_over:

    print("\nWord: ", " ".join(display))
    print(f"Lives Remaining: {lives}")

    guess = input("Guess a letter: ").lower()

    # ---------------- INPUT VALIDATION ----------------

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter an alphabet only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # ---------------- CHECK LETTER ----------------

    if guess in chosen_word:

        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        print("Correct!")

    else:

        lives -= 1
        print("Wrong Guess!")

    # ---------------- PRINT HANGMAN ----------------

    print(stages[6 - lives])

    # ---------------- WIN CONDITION ----------------

    if "_" not in display:
        game_over = True

        print("\nCongratulations! You Win!")
        print("The word was:", chosen_word)

    # ---------------- LOSE CONDITION ----------------

    if lives == 0:
        game_over = True

        print("Game Over!")
        print("You Lose!")
        print("The word was:", chosen_word)
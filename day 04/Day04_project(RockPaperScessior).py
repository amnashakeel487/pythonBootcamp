rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_choice not in [0, 1, 2]:
    print("Invalid choice! Please enter 0, 1, or 2.")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("Rock beats Scissors. You Win!")

    elif user_choice == 2 and computer_choice == 1:
        print("Scissors beat Paper. You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print("Paper beats Rock. You Win!")
    else:
        print("Computer Wins!")
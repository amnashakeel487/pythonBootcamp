import random

logo = r"""
     ____  _            _     _            _       .-------.
    | __ )| | __ _  ___| | __(_) __ _  ___| | __   |A_  _  |
    |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /   |( \\/ )|
    | |_) | | (_| | (__|   < | | (_| | (__|   <    | \\  / |
    |____/|_|\__,_|\___|_|\_\| |\__,_|\___|_|\_\   |  \\/ A|
                            |_|                    `------.
    """
# Cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Deal a random card
def deal_card():
    return random.choice(cards)


# Calculate score
def calculate_score(cards):
    score = sum(cards)

    # Blackjack
    if score == 21 and len(cards) == 2:
        return 0

    # Ace becomes 1 if score > 21
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


# Compare scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"

    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"

    elif user_score == 0:
        return "Win with a Blackjack 😎"

    elif user_score > 21:
        return "You went over. You lose 😭"

    elif computer_score > 21:
        return "Opponent went over. You win 😁"

    elif user_score > computer_score:
        return "You Win 😊"

    else:
        return "You Lose 😤"


# Main game function
def play_game():
    print(logo)


    user_cards = []
    computer_cards = []
    game_over = False

    # Deal two cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")

        if computer_score == 0:
            print("Computer's first card: A")
        else:
            print(f"Computer's first card: {computer_cards[0]}")

        # End conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer plays
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n========== RESULT ==========")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


# Play again
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Auction Program!")

bids = {}
continue_bidding = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")


while continue_bidding:

    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "yes":
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
    else:
        continue_bidding = False
        find_highest_bidder(bids)
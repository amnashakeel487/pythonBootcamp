print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Calculate bill based on pizza size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid pizza size.")

# Add pepperoni cost
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

# Add extra cheese cost
if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")
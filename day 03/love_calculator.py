print("Welcome to the Love Calculator!")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = (name1 + name2).lower()

# Count letters in "TRUE"
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

# Count letters in "LOVE"
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

# Combine the two numbers
score = int(str(true) + str(love))

# Display result
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
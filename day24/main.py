# Read the list of invited names
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

# Read the starting letter template
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()

# Create a personalized letter for each name
for name in names:
    stripped_name = name.strip()  # Remove '\n'

    new_letter = letter_contents.replace("[name]", stripped_name)

    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)
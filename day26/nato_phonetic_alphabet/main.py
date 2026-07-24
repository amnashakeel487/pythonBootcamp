import pandas as pd

# ---------------- READ CSV ---------------- #

data = pd.read_csv("nato_phonetic_alphabet.csv")

# ---------------- CREATE DICTIONARY ---------------- #

phonetic_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}


# ---------------- FUNCTION ---------------- #

def generate_phonetic():
    """Convert a word into NATO phonetic alphabet."""

    while True:
        word = input("Enter a word (or type 'exit' to quit): ").upper()

        if word == "EXIT":
            print("Thanks for using the NATO Alphabet Converter!")
            break

        try:
            output = [phonetic_dict[letter] for letter in word]
            print("\nNATO Alphabet:")
            print(output)
            print()

        except KeyError:
            print("\n❌ Sorry, only letters A-Z are allowed.")
            print("Please try again.\n")


# ---------------- START PROGRAM ---------------- #

print("=" * 50)
print("      NATO PHONETIC ALPHABET CONVERTER")
print("=" * 50)

generate_phonetic()
logo = r'''
  ____                                ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __     / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|   | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |      | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|       \____|_| .__/|_| |_|\___|_|   
                                            |_|                    
'''

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(text, shift, direction):

    result = ""

    if direction == "decode":
        shift *= -1

    shift = shift % 26

    for char in text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            result += alphabet[new_position]
        else:
            result += char

    print(f"Here's the {direction}d result: {result}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction != "encode" and direction != "decode":
        print("Invalid choice!")
        continue

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")
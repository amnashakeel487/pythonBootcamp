# Write a program that prints the numbers from 1 to 100.
# Replace multiples of 3 with "Fizz", multiples of 5 with "Buzz",
# and multiples of both 3 and 5 with "FizzBuzz". Otherwise, print the number itself.

print("FizzBuzz Game")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

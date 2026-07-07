print("Sum of Even Numbers")

target = int(input("Enter a number: "))
total = 0
for number in range(2, target + 1, 2):
    total += number

print(f"The sum of even till {target} is {total}")

# METHOD 02 Alternative method
print("Sum of Even Numbers")

target = int(input("Enter a number: "))
total = 0

for number in range(1, target + 1):
    if number % 2 == 0:
        total += number
print(f"The sum of even numbers till {target} is {total}")
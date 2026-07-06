print("Welcome to the BMI Calculator!")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")

elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")

elif bmi < 35:
    print(f"Your BMI is {bmi:.2f}, you are obese.")

else:
    print(f"Your BMI is {bmi:.2f}, you are clinically obese.")
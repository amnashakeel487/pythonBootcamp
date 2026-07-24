# example 01

sentence = input("Enter a sentence: ")

# Dictionary Comprehension
result = {word: len(word) for word in sentence.split()}

print(result)

# example 02

weather_c = eval(input("Enter the dictionary: "))

weather_f = {
    day: (temp_c * 9 / 5) + 32
    for day, temp_c in weather_c.items()
}

print(weather_f)
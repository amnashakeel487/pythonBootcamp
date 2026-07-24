# example 01
# squared a number in new list
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [n*n for n in numbers]

print(squared_numbers)

# example 02
# filter out the even numbers from input

list_of_string = input().split(',')
numbers = [int(num) for num in list_of_string]
result = [num for num in numbers if num % 2 == 0]

print(result)
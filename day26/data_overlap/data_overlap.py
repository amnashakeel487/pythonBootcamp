with open("file1.txt") as file1:
    file1 = file1.readlines()

with open("file2.txt") as file2:
    file2 = file2.readlines()

result = [int(num) for num in file1 if num in file2]
print(result)

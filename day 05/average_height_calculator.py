print("Average Student Height Calculator")

student_heights = input("Enter the heights separated by spaces: ").split()

for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"Total height = {total_height}")
print(f"Number of students = {number_of_students}")
print(f"Average height = {average_height}")
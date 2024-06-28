students_height = [180, 124, 165, 173, 189, 169, 146]
number_students = 0
total_height = 0

for i in students_height:
    number_students += 1
    total_height += i

average = round(total_height / number_students)
print(f'total height = {total_height}')
print(f'number of students = {number_students}')
print(f'average height = {average}')

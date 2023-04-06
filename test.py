"""records = []
for i in range(int(input())) :
    name = input()
    score = float (input())
    records.append([name, score])

records.sort(key=lambda x: x[1])
second_lowest_grade = 0
for i in range(1, len(records)):
    if records[i][1] > records[0][1]:
        second_lowest_grade = records[i]
        print(second_lowest_grade)
        break
second_lowest_grade.sort()
ans = second_lowest_grade
print(ans)
"""
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# sort the list by grades
students.sort(key=lambda x: x[1])

# find the second lowest grade
second_lowest_grade = None
for i in range(1, len(students)):
    if students[i][1] > students[0][1]:
        second_lowest_grade = students[i][1]
        break

# find the students with the second lowest grade
students_with_second_lowest_grade = []
for student in students:
    if student[1] == second_lowest_grade:
        students_with_second_lowest_grade.append(student[0])

# sort the names of the students alphabetically
students_with_second_lowest_grade.sort()

# print the names of the students with the second lowest grade
for name in students_with_second_lowest_grade:
    print(name)

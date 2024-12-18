grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grade = {}
for index, student in enumerate(sorted(students)):
    average_grade[student] = sum(grades[index])/len(grades[index])
print(average_grade)

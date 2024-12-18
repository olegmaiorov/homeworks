"""
Практическая работа по уроку "Динамическая типизация"
"""
name = 'Oleg'
print(f'Name: {name}')
age = 25
print(f'Age: {age}')
age += 1
print(f'New age: {age}')
is_student = True
print(f'Is Student: {is_student}')

"""
Практическое задание по теме "Переменные"
"""
homeworks_completed = 12
total_time_spent = 1.5
course_title = 'Python'
time_for_one_task = total_time_spent * 60 / homeworks_completed
print(f'Курс: {course_title}, всего задач: {homeworks_completed}, затрачено часов: {total_time_spent}, среднее время выполнения {time_for_one_task / 60} часа.')


"""
Практическое задание по уроку "Строки и индексация строк"
"""

example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[int(len(example)/2):])
print(example[::-1])
print(example[1::2])
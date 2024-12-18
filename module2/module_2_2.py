numbers = [0, 0, 0]

for index, number in enumerate(numbers):
    while True:
        try:
            numbers[index] = int(input(f'Введите {index+1}-е число:\n'))
            break
        except ValueError:
            print('Неверное значение')
            continue

unique_values = len(set(numbers))
if unique_values == 3:
    print(0)
else:
    print(4-unique_values)


# if numbers[0] == numbers[1] and numbers[0] == numbers[2]:
#     print(3)
# elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
#     print(2)
# else:
#     print(0)

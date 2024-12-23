from random import randint


def get_password(number):
    password = ''
    for i in range(1, number):
        for ii in range(i + 1, number):
            if number % (i+ii) == 0:
                password += str(i)
                password += str(ii)
    return password


number = randint(3, 20)
password = get_password(number)
print(f'{number} - {password}')
# for i in range(3, 21):
#     print(f'{i} - {get_password(i)}')

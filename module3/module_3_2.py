import re

def send_email(message:str, recipient:str, sender='university.help@gmail.com'):
    pattern = r'^\S+@\S+\.(com|ru|net)$'
    if not(re.match(pattern, sender) and re.match(pattern, recipient)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return False
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return False
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return True

test_data = [
    ['Это сообщение для проверки связи', 'vasyok1337@gmail.com'],
    ['Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com'],
    ['Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk'],
    ['Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru'],
]

for parameters in test_data:
    send_email(*parameters)

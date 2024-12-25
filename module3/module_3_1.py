calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string:str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string:str, list_to_search:list):
    count_calls()
    if string.lower() in str(list_to_search).lower():
        return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', [1, 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

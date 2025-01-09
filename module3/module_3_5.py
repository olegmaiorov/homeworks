def get_multiplied_digits(number:int):
    str_number = str(number).replace('0', '')
    first = int(str_number[0])
    if len(str_number) == 1:
        return number
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(5)) # -> 5
result = get_multiplied_digits(40203)
print(result) # -> 24
result2 = get_multiplied_digits(402030)
print(result2) # -> 24

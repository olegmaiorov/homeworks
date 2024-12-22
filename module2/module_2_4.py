numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    for i in range(2, number + 1):
        if number % i == 0:
            if i == number:
                primes.append(number)
                break
            not_primes.append(number)
            break
print(primes)
print(not_primes)

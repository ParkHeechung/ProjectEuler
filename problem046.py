from util import get_primes

def get_composite_numbers(number):
    composite_numbers = []
    primes = get_primes(number)
    for i in range(2, number + 1):
        if 2 * i - 1 not in primes:
            composite_numbers.append(2 * i - 1)
    return composite_numbers
            

def get_square_numbers(number):
    square_numbers = []
    for j in range(1, number + 1):
        square_numbers.append(j**2)
    return square_numbers

composite_numbers = get_composite_numbers(100000)
primes = get_primes(100000)
for num1 in composite_numbers:
    for num2 in primes:
        square_numbers = get_square_numbers(100000)
        if (num1 - num2) // 2 not in square_numbers:
            print(num1)


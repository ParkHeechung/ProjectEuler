from util import get_primes

def get_odd_composite_numbers(n, primes_set):
    odd_composite_numbers = []
    for number in range(2, n):
        if number % 2 == 1 and number not in primes_set:
            odd_composite_numbers.append(number) 
    return odd_composite_numbers

def check_combination(odd_composite_number, primes, squares):
    has_combination = False
    for square in squares:
        if (odd_composite_number - 2 * square) in primes:
            has_combination = True
            break
    return has_combination
        

primes = set(get_primes(10**7))
odd_composite_numbers = get_odd_composite_numbers(10**7, primes)
squares = list(map(lambda x: x**2, range(1, 10**4)))

answer = -1
for odd_composite_number in odd_composite_numbers:
    has_combination = check_combination(odd_composite_number, primes, squares)
    if not has_combination:
        answer = odd_composite_number
        break

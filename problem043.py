from itertools import permutations
from util import get_primes

def check_all_pandigital(number):
    primes = get_primes(18)
    all_pandigital = True
    number_str = str(number)
    for n in range(1, 8):
        if int(number_str[n:n+3]) % primes[n-1] != 0:
            all_pandigital = False
            break
    return all_pandigital

pandigital_numbers = list(permutations(range(10), 10))
all_pandigital_number = []
for i in pandigital_numbers:
    pandigital_number = "".join(str(j) for j in i)
    all_pandigital = check_all_pandigital(pandigital_number)
    if all_pandigital:
        all_pandigital_number.append(pandigital_number)
        
sum_answer = 0
for number in all_pandigital_number:
    sum_answer += int(number)
    answer = sum_answer

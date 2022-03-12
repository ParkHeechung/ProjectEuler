from itertools import permutations

from euler_util import get_primes, tuple_to_int

def check_permuation_primes(prime, primes_set):
    result = []
    prime_str = str(prime)
    permutation = list(permutations(prime_str, len(prime_str)))
    permutation_int = set(map(lambda x: tuple_to_int(x), permutation))
    for interval in range(1, 3334):
        found = True
        for count in range(1, 3):
            check_num = prime + count*interval
            if 10000 <= check_num :
                found = False
                break
            if check_num not in primes_set or check_num not in permutation_int:
                found = False
                break
        if found:
            for count in range(3):
                check_num = prime + count*interval
                result.append(check_num)
            break
    return result
        

primes = get_primes(10**4)
primes_set = set(primes)
result = []
for prime in primes:
    permutation_primes = check_permuation_primes(prime, primes_set)
    if permutation_primes:
        result.append(permutation_primes)
        
answer = ""
for number in result[-1]:
    answer += str(number)
    
####

from itertools import permutations

from euler_util import get_primes, tuple_to_int

def get_permuation_primes(prime, primes_set):
    permuation_primes = []
    prime_str = str(prime)
    permutation = list(permutations(prime_str, len(prime_str)))
    permutation_int = set(map(lambda x: tuple_to_int(x), permutation))
    for interval in range(1, 3334):
        is_matched = check_conditions(prime, interval, primes_set, permutation_int)
        if is_matched:
            permuation_primes = get_interval_numbers(prime, interval)
            break
    return permuation_primes

def check_conditions(prime, interval, primes_set, permutation_int):
    found = True
    for count in range(1, 3):
        check_num = prime + count*interval
        if 10000 <= check_num :
            found = False
            break
        if check_num not in primes_set or check_num not in permutation_int:
            found = False
            break
    return found

def get_interval_numbers(prime, interval):
    interval_numbers = []
    for count in range(3):
        number = prime + count*interval
        interval_numbers.append(number)
    return interval_numbers

primes = get_primes(10**4)
primes_set = set(primes)
result = []
for prime in primes:
    permutation_primes = get_permuation_primes(prime, primes_set)
    if permutation_primes:
        result.append(permutation_primes)
        
answer = ""
for number in result[-1]:
    answer += str(number)
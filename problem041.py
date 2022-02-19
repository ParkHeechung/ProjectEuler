from util import get_primes

def check_all_digits(numbers):
    numbers_str = str(numbers)
    numbers_set = set()
    for digit in numbers_str:
        numbers_set.add(int(digit))
        
    has_all_digits = True
    for digit in range(1, len(numbers_str)+1):
        if digit not in numbers_set:
            has_all_digits = False
            break
    return has_all_digits
                
primes = set(get_primes(10**7))
biggest_answer = 0
for number in primes:
    has_all_digits = check_all_digits(number)
    if has_all_digits:
        if biggest_answer < number:
            biggest_answer = number
            
assert check_all_digits(2143) == True
assert check_all_digits(1232) == False
assert check_all_digits(982734156) == True

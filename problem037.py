from util import get_primes

def create_numbers_removing_ciphers(number):
    number_str = str(number)
    numbers_removing_ciphers = set()
    for index in range(len(number_str)):
        number_removing_ciphers1 = int(number_str[index::])
        numbers_removing_ciphers.add(number_removing_ciphers1)
        number_removing_ciphers2 = int(number_str[:index+1])
        numbers_removing_ciphers.add(number_removing_ciphers2)        
    return numbers_removing_ciphers

def check_removing_ciphers_prime(number, primes):
    numbers_removing_ciphers = create_numbers_removing_ciphers(number)
    is_removing_ciphers_prime = True
    for number in numbers_removing_ciphers:
        if number not in primes:
            is_removing_ciphers_prime = False
            break
    return is_removing_ciphers_prime

primes = set(get_primes(10**7))
answer_sum = 0
for number in primes:
    is_removing_ciphers_prime = check_removing_ciphers_prime(number, primes)
    if is_removing_ciphers_prime:
        answer_sum += number
    print(answer_sum - 17)

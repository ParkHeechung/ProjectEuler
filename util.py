def get_factorial(number):
    factorial = 1
    for n in range(1, number + 1):
        factorial *= n
    return factorial

def is_prime(number):
    if number <= 0:
        return False
    is_prime = True
    root_of_number = number ** 0.5
    for candidate_factor in range(2, int(root_of_number) + 1):
        if number % candidate_factor == 0:
            is_prime = False
            break
    if number == 2:
        is_prime = True
    return is_prime

def get_primes(limit):
    primes = []
    sieve = [True]*limit
    sieve[0] = False
    sieve[1] = False
    for number, is_prime in enumerate(sieve):
        if is_prime:
            primes.append(number)
            for index in range(number*number, limit, number):
                sieve[index] = False
    return primes
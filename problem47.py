from euler_util import get_primes

def get_prime_factors(target, primes, primes_set):
    prime_factors = set()
    while True:
        for prime in primes:
            if target % prime == 0:
                target = target // prime
                prime_factors.add(prime)
                break
        if target == 1:
            break
    return prime_factors

target_count = 4
primes = get_primes(10**7)
primes_set = set(primes)
consecutive_count = 0
for number in range(1, 10**7):
    prime_factors = get_prime_factors(number, primes, primes_set)
    if len(prime_factors) == target_count:
        consecutive_count += 1
    else:
        consecutive_count = 0
    if consecutive_count == target_count:
        answer = number - target_count + 1
        break

if consecutive_count == target_count:
    print(answer)
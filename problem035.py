from util import get_primes

def create_circular_numbers(number):
    number_str = str(number)
    circular_numbers = []
    for index in range(len(number_str)):
        circular_number = int(number_str[index:] + number_str[:index])
        circular_numbers.append(circular_number)
    return circular_numbers

def check_circular_prime(number, primes):
    circular_numbers = create_circular_numbers(number)
    is_circular_prime = True
    for number in circular_numbers:
        if number not in primes:
            is_circular_prime = False
            break
    return is_circular_prime

def main(): #시간 재기 - 콘솔창에 %time main() 엔터
    primes = set(get_primes(10**7))
    count = 0
    for number in range(10**7):
        is_circular_prime = check_circular_prime(number, primes)
        if is_circular_prime:
            count += 1
    print(count)
from util import get_factorial

def get_cipher_factorial_sum(number):
    cipher_factorial_sum = 0
    for i in str(number):
        cipher_factorial_sum += get_factorial(int(i))
    return cipher_factorial_sum

answer = 0
for number in range(1, 1000000):
    cipher_factorial_sum = get_cipher_factorial_sum(number)
    if cipher_factorial_sum == number:
        answer += number
    print(answer - 3)
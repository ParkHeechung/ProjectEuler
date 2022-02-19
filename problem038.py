def create_until_digit_duplication(number):
    numbers = []
    digits = set()
    n = 1
    while True:
        next_number = number*n
        next_number_str = str(next_number)
        has_duplicated_digits = check_digit_duplication(next_number_str, digits)
        if has_duplicated_digits:
            break
        digits = add_digits(next_number_str, digits)
        numbers.append(next_number)
        n += 1
    return numbers

def check_digit_duplication(number_str, digits):
    digits = set(digits)
    has_duplicated_digits = False
    for char in number_str:
        if char in digits and char != "0":
            has_duplicated_digits = True
            break
        else:
            digits.add(char)
    return has_duplicated_digits

def add_digits(next_number_str, digits):
    for char in next_number_str:
        digits.add(char)
    return digits

def get_pandigital_multiples():
    pandigital_multipiles = []
    for number in range(1, 10**5):
        numbers = create_until_digit_duplication(number)
        result = "".join(map(str, numbers))
        if len(result) == 9:
            pandigital_multipiles.append(numbers)
    return pandigital_multipiles

pandigital_multipiles = get_pandigital_multiples()
answer = "".join(map(str, pandigital_multipiles[-1]))
def get_triangle_number(number):
    triangle_numbers = []
    for n in range(1, number +1):
        triangle_number = n * (n + 1) // 2
        triangle_numbers.append(triangle_number)
    return triangle_numbers

def get_pentagonal_number(number):
    pentagonal_numbers = []
    for n in range(1, number +1):
        pentagonal_number = n * (n * 3 - 1) // 2
        pentagonal_numbers.append(pentagonal_number)
    return pentagonal_numbers

def get_hexagonal_number(number):
    hexagonal_numbers = []
    for n in range(1, number +1):
        hexagonal_number = n * (n * 2 - 1)
        hexagonal_numbers.append(hexagonal_number)
    return hexagonal_numbers

answers = []
triangle_numbers = get_triangle_number(1000000)
pentagonal_numbers = set(get_pentagonal_number(1000000))
hexagonal_numbers = set(get_hexagonal_number(1000000))
for number in triangle_numbers:
    if number in pentagonal_numbers:
        if number in hexagonal_numbers:
            answers.append(number)
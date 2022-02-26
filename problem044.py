def get_pentagonal_number(number):
    pentagonal_numbers = []
    for n in range(1, number +1):
        pentagonal_number = n * (n * 3 - 1) // 2
        pentagonal_numbers.append(pentagonal_number)
    return pentagonal_numbers


smallest_answer = float(10000000)
pentagonal_numbers = get_pentagonal_number(10000)
pentagonal_number_set = set(pentagonal_numbers)
for k in range(10000):
    for j in range(10000):
        p_j = pentagonal_numbers[j]
        p_k = pentagonal_numbers[k]
        if p_j + p_k in pentagonal_number_set and p_j - p_k in pentagonal_number_set:
            print(p_j - p_k)

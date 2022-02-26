def get_pentagonal_number(number):
    pentagonal_number_set = set()
    for n in range(1, number +1):
        pentagonal_number = n * (n * 3 - 1) / 2
        pentagonal_number_set.add(pentagonal_number)
    return pentagonal_number_set


smallest_answer = float(10000000)
pentagonal_number_set = get_pentagonal_number(1000)
for k in range(1000):
    for j in range(1000):
        if k * (k * 3 - 1) / 2 + j * (j * 3 - 1) / 2 in pentagonal_number_set:
            if k * (k * 3 - 1) / 2 - j * (j * 3 - 1) / 2 in pentagonal_number_set:
                if k * (k * 3 - 1) / 2 - j * (j * 3 - 1) / 2 < smallest_answer:
                    smallest_answer = k * (k * 3 - 1) / 2 - j * (j * 3 - 1) / 2
print(smallest_answer)

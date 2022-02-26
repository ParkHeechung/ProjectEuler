from itertools import permutations

pandigital_numbers = list(permutations(range(10), 10))
pandigital_number = ()
for i in pandigital_numbers:
    pandigital_number = "".join(str(j) for j in i)
    pandigital_number.append(pandigital_number)
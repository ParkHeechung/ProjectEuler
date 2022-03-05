number = 0
for n in range(1, 1000):
    number += n ** n
print(str(number)[-10:])
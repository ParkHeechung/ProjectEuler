answer = 0
for number in range(1, 1000000):
    if str(number) == str(number)[::-1]:
        if str(bin(number)[2:]) == str(bin(number)[2:][::-1]):
            answer += number
        print(answer)

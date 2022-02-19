champernownes_constant = "0."
for number in range(1, 10**6):
    champernownes_constant += str(number)
answer = int(champernownes_constant[2]) * int(champernownes_constant[11]) * int(champernownes_constant[101]) * int(champernownes_constant[1001]) * int(champernownes_constant[10001]) * int(champernownes_constant[100001]) * int(champernownes_constant[1000001]) 

####
answer = 1
for n in range(7):
    d_n = champernownes_constant[10**n + 1]
    answer *= int(d_n)
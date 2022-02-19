for p in range(3, 1000):
    p_count = 0
    for c in range(1, 333):
        for a in range(1, c):
            b = p - c - a
            if b == (c**2 - a**2)**0.5:
                p_count += 1
            if c <= b:
                break
            
max_p_count = 0
if max_p_count < p_count:
   p_count = max_p_count
print(max_p_count)
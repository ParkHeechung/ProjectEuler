from collections import Counter

counter = Counter()
triangles = []
for a in range(1, 500):
    for b in range(1, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c:
            if a + b + c <= 1000:
                counter[a + b + c] += 1
most_common = counter.most_common(1)
answer = most_common[0][0]
                     
                 
# from collections import Counter

# counter = Counter()
# triangles = [10, 12, 12, 14, 16, 18, 20, 14, 14, 10]
# for p in triangles:
#     counter[p] += 1
# most_common = counter.most_common(1)
# answer = most_common[0][0]

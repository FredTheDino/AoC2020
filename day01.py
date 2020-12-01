from itertools import combinations

numbers = []
while True:
    try:
        n = int(input())
    except:
        break
    numbers.append(n)

def comb(xs, n):
    for i, x in enumerate(xs):
        for res in comb(xs[i:], n - 1):
            ...


for a, b in combinations(numbers, 2):
    if a + b == 2020:
        print(a * b)
        break

for a, b, c in combinations(numbers, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break

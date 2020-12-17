import sys
from itertools import combinations
from time import time

numbers = [int(x) for x in sys.stdin.readlines()]

# Part 1
def p1():
    for n in range(len(numbers)):
        expected = numbers[n+25]
        for a, b in combinations(numbers[n:n+25], 2):
            if a + b == expected:
                break
        else:
            invalid = expected
            break
    return invalid

invalid = p1()
print(invalid)


# Part 2
def p2(invalid):
    start = 0
    end = 0
    total = 0
    while total != invalid or abs(start - end) < 2:
        if total > invalid:
            total -= numbers[start]
            start += 1
        else:
            total += numbers[end]
            end += 1

    return min(numbers[start:end]) + max(numbers[start:end])

print(p2(invalid))


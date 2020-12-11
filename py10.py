import sys
from functools import cache

numbers = set(int(x) for x in sys.stdin.readlines())

# Part 1
jolt_diff = [0, 0, 0]
jolt = 0
while True:
    if jolt + 1 in numbers:
        jolt += 1
        jolt_diff[0] += 1
    elif jolt + 2 in numbers:
        jolt += 2
        jolt_diff[1] += 1
    elif jolt + 3 in numbers:
        jolt += 3
        jolt_diff[2] += 1
    else:
        break

jolt += 3
jolt_diff[2] += 1

numbers.add(jolt)

print(jolt_diff[0] * jolt_diff[2])


# Part 2

# The slow way
@cache
def count_paths(jolt):
    if jolt == 0:
        return 1
    if jolt not in numbers:
        return 0
    return sum(count_paths(jolt - o) for o in [1, 2, 3])

print(count_paths(max(numbers)))

# The faster way
# counts = [0] * (max(numbers) + 1)
# counts[0] = 1
# for n in sorted(numbers):
#     ways = 0
#     if n > 2:
#         ways += counts[n - 3]
#     if n > 1:
#         ways += counts[n - 2]
#     ways += counts[n - 1]
#     counts[n] = ways
# print(counts[max(numbers)])

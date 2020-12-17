import sys
from itertools import product

def tuple_add(a, b):
    return tuple(map(sum, zip(a, b)))

active = set()
for y, line in enumerate(sys.stdin.readlines()):
    for x, c in enumerate(line):
        if c == "#":
            active.add((x, y, 0))
lo = (-1, -1, -1)
hi = (x + 1, y + 1, 1)

def neighbors(p, dim):
    for d in product([-1, 0, 1], repeat=dim):
        if all(x == 0 for x in d):
            continue
        yield tuple_add(p, d)


def step(active, lo, hi, dim):
    next_active = set()
    for p in product(*[range(a, b + 1) for a, b in zip(lo, hi)]):
        num_active = sum(n in active for n in neighbors(p, dim=dim))
        if p in active and num_active in [2, 3]:
            next_active.add(p)
        elif p not in active and num_active == 3:
            next_active.add(p)

    return next_active, tuple_add(lo, tuple([-1] * dim)), tuple_add(hi, tuple([1] * dim))


def solve(active, lo, hi):
    for _ in range(6):
        active, lo, hi = step(active, lo, hi, len(hi))
    print(len(active))

solve(active, lo, hi)
solve(set((*t, 0) for t in active), (*lo, -1), (*hi, 1))


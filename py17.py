import sys
from itertools import product
from functools import cache
from collections import defaultdict

def tuple_add(a, b):
    return tuple(map(sum, zip(a, b)))

@cache
def neighbors(p):
    return [tuple_add(p, d)
            for d in product([-1, 0, 1], repeat=len(p))
            if not all(x == 0 for x in d)]


def update(counts, active, p, alive):
    if alive and p in active:
        return

    if not alive and p not in active:
        return

    delta = 1 if alive else -1
    for n in neighbors(p):
        counts[n] += delta


active3 = set()
counts3 = defaultdict(int)
active4 = set()
counts4 = defaultdict(int)

for y, line in enumerate(sys.stdin.readlines()):
    for x, c in enumerate(line):
        if c == "#":
            p = x, y, 0

            # It'll be out little secret...
            active3.add(p)
            for n in neighbors(p):
                counts3[n] += 1

            active4.add((*p, 0))
            for n in neighbors((*p, 0)):
                counts4[n] += 1


def step(active, counts):
    next_counts = counts.copy()
    next_active = active.copy()

    for p, count in counts.items():
        alive = ((p in active and 2 <= count <= 3) or
                 (p not in active and count == 3))

        if alive and p in active:
            continue

        if not alive and p not in active:
            continue

        if alive:
            delta = 1
            next_active.add(p)
        else:
            delta = -1
            next_active.remove(p)

        for n in neighbors(p):
            next_counts[n] += delta

    return next_active, next_counts


def solve(active, counts):
    for _ in range(6):
        active, counts = step(active, counts)
    print(len(active))

solve(active3, counts3)

solve(active4, counts4)


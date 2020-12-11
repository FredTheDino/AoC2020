import sys
from functools import cache

seats = {}
region = (0, 0)
for y, line in enumerate(sys.stdin.readlines()):
    for x, c in enumerate(line):
        if c == ".":
            continue
        seats[x, y] = c
        region = max(region[0], x), max(region[1], y)
orignal_seats = seats.copy()

def simulate_1(in_seats):
    def count_occupied(seats, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                seat = x + dx, y + dy
                if seat in seats:
                    count += seats[seat] == "#"
        return count

    modified = False
    out_seats = {}
    for p, state in in_seats.items():
        occupied = count_occupied(in_seats, *p)
        if state == "L" and occupied == 0:
            out_seats[p] = "#"
            modified = True
        elif state == "#" and occupied >= 4:
            out_seats[p] = "L"
            modified = True
        else:
            out_seats[p] = state
    return out_seats, modified

def show(seats):
    highest = max(seats.keys())
    for y in range(0, highest[1] + 1):
        for x in range(0, highest[0] + 1):
            if (x, y) in seats:
                print(seats[x, y], end="")
            else:
                print(" ", end="")

modified = True
while modified:
    seats, modified = simulate_1(seats)
print(sum(c == "#" for c in seats.values()))


@cache
def visable_seats(x, y):
    visable = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            for step in range(1, 100000):
                seat = x + dx * step, y + dy * step
                if seat[0] < 0 or seat[1] < 0:
                    break
                if seat[0] > region[0] or seat[1] > region[1]:
                    break
                if seat in seats:
                    visable.append(seat)
                    break
    return visable


def simulate_2(in_seats):
    def count_occupied(seats, x, y):
        return sum(seats[p] == "#" for p in visable_seats(x, y))

    modified = False
    out_seats = {}
    for p, state in in_seats.items():
        occupied = count_occupied(in_seats, *p)
        if state == "L" and occupied == 0:
            out_seats[p] = "#"
            modified = True
        elif state == "#" and occupied >= 5:
            out_seats[p] = "L"
            modified = True
        else:
            out_seats[p] = state
    return out_seats, modified

# 2278 - Too high

seats = orignal_seats.copy()
modified = True
while modified:
    seats, modified = simulate_2(seats)
print(sum(c == "#" for c in seats.values()))

import sys

def from_dir(n):
    return [(1, 0), (0, -1), (-1, 0), (0, 1)][n % 4]

moves = [(inst[0], int(inst[1:])) for inst in sys.stdin.readlines()]

def solve1():
    pos = (0, 0)
    dir = 0
    for d, n in moves:
        if d == "L":
            assert n % 90 == 0
            dir -= n // 90
            continue
        elif d == "R":
            assert n % 90 == 0
            dir += n // 90
            continue
        elif d == "F":
            delta = from_dir(dir)
        elif d == "N":
            delta = (0, 1)
        elif d == "S":
            delta = (0, -1)
        elif d == "W":
            delta = (-1, 0)
        elif d == "E":
            delta = (1, 0)
        x, y = pos
        dx, dy = delta
        pos = x + n * dx, y + n * dy
    x, y = pos
    print(abs(x) + abs(y))
solve1()


def rotate_ccw(a, b):
    return -b, a

def rotate_cw(a, b):
    return b, -a

def solve2():
    way_point = (10, 1)
    pos = (0, 0)
    dir = 0
    for d, n in moves:
        if d == "L":
            for _ in range((n // 90) % 4):
                way_point = rotate_ccw(*way_point)
        elif d == "R":
            for _ in range((n // 90) % 4):
                way_point = rotate_cw(*way_point)
        elif d == "N":
            way_point = way_point[0], way_point[1] + n
        elif d == "S":
            way_point = way_point[0], way_point[1] - n
        elif d == "W":
            way_point = way_point[0] - n, way_point[1]
        elif d == "E":
            way_point = way_point[0] + n, way_point[1]
        elif d == "F":
            x, y = pos
            dx, dy = way_point
            pos = x + n * dx, y + n * dy
    x, y = pos
    print(abs(x) + abs(y))

solve2()

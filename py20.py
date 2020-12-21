from itertools import product, combinations, repeat
from collections import defaultdict
import sys

edges = defaultdict(set)
tiles = {}

for tile in sys.stdin.read().split("\n\n"):
    tile_id = None
    data = []
    for line in tile.split("\n"):
        if line.strip() == "":
            continue
        if "Tile" in line:
            tile_id = int(line.split(" ")[1][:-1])
        else:
            data.append(line)

    if not data:
        continue

    north = data[0]
    south = data[-1]
    west = ""
    east = ""

    for line in data:
        west += line[0]
        east += line[-1]

    def first(x):
        return sorted([x, x[::-1]])[0]

    north = first(north)
    south = first(south)
    west = first(west)
    east = first(east)

    edges[north].add(tile_id)
    edges[east].add(tile_id)
    edges[south].add(tile_id)
    edges[west].add(tile_id)
    tiles[tile_id] = north, east, south, west, data

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

possible = {}
for id, (n, e, s, w, _) in tiles.items():
    possible[id] = [
        edges[n] - set([id]),
        edges[e] - set([id]),
        edges[s] - set([id]),
        edges[w] - set([id]),
    ]

def all_orientations(n, e, s, w):
    yield n, e, s, w, ""
    yield w, n, e, s, "r"
    yield s, w, n, e, "rr"
    yield e, s, w, n, "rrr"

    yield s, e, n, w, "f"
    yield w, s, e, n, "fr"
    yield n, w, s, e, "frr"
    yield e, n, w, s, "frrr"


def solve(x, y, tiles, reqs, position):
    w = len(tiles) ** 0.5
    if w <= x:
        return True

    if w <= y:
        return True

    if (x, y) in position:
        return True

    any_key = set(tiles.keys())
    left = (x - 1, y), EAST
    top  = (x, y - 1), SOUTH
    alts = reqs.get(left, any_key) & reqs.get(top, any_key)

    for id in alts:
        if x == 0 and y == 0:
            neigbors = sum(map(len, reqs[id]))
            if 1 + 1 + 0 + 0 != neigbors:
                continue

        for n, e, s, w, o in all_orientations(*reqs[id]):
            if x == 0 and len(w) != 0:
                continue
            if y == 0 and len(n) != 0:
                continue

            expected = position.get((x, y - 1), None)
            if expected and expected[0] not in n:
                continue

            expected = position.get((x - 1, y), None)
            if expected and expected[0] not in w:
                continue

            reqs_c = reqs.copy()
            pos_c = position.copy()

            reqs_c[(x, y), EAST]  = e
            reqs_c[(x, y), SOUTH] = s
            pos_c[x, y] = id, o

            if not solve(x + 1, y, tiles, reqs_c, pos_c):
                continue
            if not solve(x, y + 1, tiles, reqs_c, pos_c):
                continue

            position.update(pos_c)

            return True
    return False


# 46333628948161 -- Too high
positions = {}
result = solve(0, 0, tiles, possible, positions)
lo, hi = 0, max(positions.keys())[0]
prod = 1
for p in product([lo, hi], repeat=2):
    prod *= positions[p][0]
print(prod)

def strip(data):
    return [c[1:-1] for c in data[1:-1]]

def flip_h(data):
    return [c[::-1] for c in data]

def flip_v(data):
    return data[::-1]

def rotate(data):
    return ["".join(c) for c in zip(*list(data)[::-1])]

transformed_tiles = {}
for x in range(lo, hi + 1):
    for y in range(lo, hi + 1):
        id, o = positions[x, y]
        tile = tiles[id][4]

        for c in o:
            if "f" == c:
                tile = flip_v(tile)
            else:
                tile = rotate(tile)

        if y != 0:
            prev = transformed_tiles[x, y - 1][-1]
            if prev != tile[0] and y != 0:
                tile = flip_h(tile)
        transformed_tiles[x, y] = tile

full = ["" for y in range((hi + 1) * 8)]
for x in range(lo, hi + 1):
    for y in range(lo, hi + 1):
        tile = strip(transformed_tiles[x, y])
        for ey, row in enumerate(tile):
            full[y * 8 + ey] += row

# print("\n".join(full))

def tuple_add(a):
    return tuple(map(sum, zip(*a)))

monster = \
"""
                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""
monster = [(x, y - 1)
           for y, line in enumerate(monster.split("\n"))
           for x, c in enumerate(line) if c == "#"]

from copy import deepcopy

for _, _, _, _, o in all_orientations(None, None, None, None):
    ghost = deepcopy(full)
    for c in o:
        if "f" == c:
            ghost = flip_v(ghost)
        else:
            ghost = rotate(ghost)

    seamonsters = set()
    for y in range(lo, len(ghost) - 2):
        for x in range(lo, len(ghost) - 19):
            monster_pos = set(map(tuple_add, zip(repeat((x, y)), monster)))
            if all(ghost[y][x] == "#" for x, y in monster_pos):
                seamonsters = seamonsters | monster_pos

    if not seamonsters:
        continue

    count = 0
    for y, line in enumerate(ghost):
        for x, c in enumerate(line):
            if c == "#" and (x, y) not in seamonsters:
                count += 1
    print(count)

    # for y, line in enumerate(ghost):
    #     for x, c in enumerate(line):
    #         if (x, y) in seamonsters:
    #             print("O", end="")
    #         elif c == "#":
    #             print("~", end="")
    #         elif c == ".":
    #             print(" ", end="")
    #     print()

# 2716 Too high?
# 2727 Is wrong
# 2729 Too high
# 2757 Is wrong
# 2817 Too high

from itertools import product
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
            if expected and expected not in n:
                continue

            expected = position.get((x - 1, y), None)
            if expected and expected not in w:
                continue

            reqs_c = reqs.copy()
            pos_c = position.copy()

            reqs_c[(x, y), EAST]  = e
            reqs_c[(x, y), SOUTH] = s
            pos_c[x, y] = (id, o)

            if not solve(x + 1, y, tiles, reqs_c, pos_c):
                continue
            if not solve(x, y + 1, tiles, reqs_c, pos_c):
                continue

            position.update(pos_c)

            return True
    return False


positions = {}
result = solve(0, 0, tiles, possible, positions)
lo, hi = 0, max(positions.keys())[0]
prod = 1
for p in product([lo, hi], repeat=2):
    prod *= positions[p][0]
print(prod)


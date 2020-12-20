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
    tiles[tile_id] = north, east, south, west


def match(args):
    a, b = args
    return a == b or b is None or a is None


def all_orientations(n, e, s, w):
    yield n, e, s, w
    yield w, n, e, s
    yield s, w, n, e
    yield e, s, w, n

    yield s, e, n, w
    yield w, s, e, n
    yield n, w, s, e
    yield e, n, w, s


def get_neighbors(x, y):
    yield x, y + 1
    yield x + 1, y
    yield x, y - 1
    yield x - 1, y


def get_adjecant(x, y):
    yield x, y + 1, 2
    yield x + 1, y, 3
    yield x, y - 1, 0
    yield x - 1, y, 1


def solve(x, y, tiles, edges, placed, used, position):
    if x < 0 or (len(tiles) ** 0.5) <= x:
        return True

    if y < 0 or (len(tiles) ** 0.5) <= y:
        return True

    if (x, y, 0) in placed:
        return True

    given = []
    if placed:
        possible = None
        for p in get_adjecant(x, y):
            conn = placed.get(p, None)
            given.append(conn)

            if conn:
                if possible is None:
                    possible = edges[conn].copy()
                else:
                    possible = possible & edges[conn]
        possible -= used
    else:
        possible = tiles.keys()
        given = [None] * 4

    for id in possible:
        for sides in all_orientations(*tiles[id]):
            if not all(map(match, zip(sides, given))):
                continue

            used.add(id)
            positions[x, y] = id
            placed[x, y, 0] = sides[0]
            placed[x, y, 1] = sides[1]
            placed[x, y, 2] = sides[2]
            placed[x, y, 3] = sides[3]

            for nx, ny in get_neighbors(x, y):
                if not solve(nx, ny, tiles, edges, placed, used, positions):
                    break
            else:
                return True

            del positions[x, y]
            del placed[x, y, 0]
            del placed[x, y, 1]
            del placed[x, y, 2]
            del placed[x, y, 3]
            used.remove(id)
    return False


# 46333628948161 -- Too high
positions = {}
placed = {}
used = set()
result = solve(0, 0, tiles, edges, placed, used, positions)
print(result, placed)
print(positions[0, 0] * positions[0, 11] * positions[11, 0] * positions[0, 0])

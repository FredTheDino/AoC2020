def number_gen(step=1):
    n = 0
    while True:
        yield n
        n += step


def parse_stdin():
    width = 0
    height = 0
    trees = set()
    for y in number_gen():
        try:
            line = input()
        except Exception as e:
            break
        width = len(line)
        height = y + 1
        for x, c in enumerate(line):
            if c == "#":
                trees.add((x, y))
    return width, height, trees


def count_hits(w, h, dx, dy, ts):
    hits = 0
    for x, y in zip(number_gen(dx), number_gen(dy)):
        if y > h: break
        hits += (x % w, y) in ts
    return hits

if __name__ == "__main__":
    w, h, ts = parse_stdin()

    print(count_hits(w, h, 3, 1, ts))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for x, y in slopes:
        prod *= count_hits(w, h, x, y, ts)
    print(prod)

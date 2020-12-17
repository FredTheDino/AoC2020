from itertools import count

# TODO(ed): Parse input
raw = list(enumerate(map(int, input().split(","))))

def f(end):
    said = {n: t + 1 for t, n in raw}
    last, start = max(said.items(), key=lambda x: x[1])
    del said[last]
    i = start + 1
    while i <= end:
        last_i = said.get(last, None)
        if last_i is None:
            new = 0
        else:
            new = i - last_i - 1
        said[last] = i - 1
        last = new
        i += 1

    print(last)

f(2020)
f(30000000)

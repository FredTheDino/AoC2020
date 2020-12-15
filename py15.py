from itertools import count

# TODO(ed): Parse input
raw = list(enumerate(map(int, input().split(","))))

said = {n: t + 1 for t, n in raw}
last, start = max(said.items(), key=lambda x: x[1])
del said[last]
for i in range(start+1, 30000000 + 1):
    last_i = said.get(last, None)
    if last_i is None:
        new = 0
    else:
        new = i - last_i - 1
    said[last] = i - 1
    last = new
    if i == 2020:
        print(last)
    if i == 30000000:
        print(last)


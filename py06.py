import sys
from functools import reduce

anyyes = []
allyes = []
for group in sys.stdin.read().split("\n\n"):
    toutlesyes = set(group.replace("\n", ""))
    anyyes.append(toutlesyes)
    allyes.append(reduce(lambda a, b: a.intersection(b),
                         map(set, group.split("\n")),
                         toutlesyes))

print(sum(map(lambda x: len(x), anyyes)))

print(sum(map(lambda x: len(x), allyes)))

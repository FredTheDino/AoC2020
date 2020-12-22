import sys

ingridients = {}
allergants = {}
all_ingredients = set()
foods = []
for line in sys.stdin.readlines():
    simplified = line.replace(",", "").replace("(", "").replace(")", "")
    assert "contains" in simplified
    ingr, aller = simplified.split("contains")
    ingr  = set(ingr.split())
    aller = set(aller.split())

    for a in aller:
        if a not in allergants:
            allergants[a] = ingr.copy()
        else:
            allergants[a] &= ingr

    all_ingredients |= ingr
    foods.append(ingr)

possible = set()
for x in allergants.values():
    possible |= x

print(sum(x not in possible for food in foods for x in food))

change = True
while change:
    change = False
    for outer, outer_possible in allergants.items():
        if len(outer_possible) == 1:
            ingr = list(outer_possible)[0]
            for inner, inner_possible in allergants.items():
                if inner == outer:
                    continue
                if ingr in inner_possible:
                    allergants[inner].remove(ingr)
                    change = True

print(",".join(list(map(lambda x: list(x[1])[0], sorted(allergants.items())))))

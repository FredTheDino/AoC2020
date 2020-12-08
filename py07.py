import sys

bagtree = {}
for rule in sys.stdin.read().split("\n"):
    if rule.strip() == "":
        continue
    bag, inside = rule.split(" contain ")
    requirements = []
    if "no other bags" in inside:
        requirements = []
    else:
        for a in inside.split(","):
            n, qual, col = a.strip().split(" ")[:3]
            requirements.append((int(n), qual + col))
    name = "".join(bag.split()[:2])
    bagtree[name] = requirements

def parents(tree, target, found=None):
    if found is None:
        found = set()

    found.add(target)
    for bag, insides in tree.items():
        if target in [c for _, c in insides]:
            parents(tree, bag, found)
    return found

print(len(parents(bagtree, "shinygold")) - 1)

def count_children(tree, target):
    children = 0
    for bag, insides in tree.items():
        if bag == target:
            for n, color in insides:
                children += n * (1 + count_children(tree, color))
    return children

print(count_children(bagtree, "shinygold"))

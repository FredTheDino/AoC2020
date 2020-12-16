import sys
from functools import reduce

def gen_range(range_str):
    lo, hi = map(int, range_str.strip().split("-"))
    return list(range(lo, hi + 1))

rules = {}
tickets = []
my_ticket = None
section = 0
for line in sys.stdin.readlines():
    if not line.strip():
        section += 1
        continue

    if section == 0:  # Rules
        name, value = line.split(":")
        a, b = value.split("or")
        rules[name] = set([*gen_range(a), *gen_range(b)])

    # Skipp headers
    if ":" in line: continue

    if section == 1:  # My ticket
        my_ticket = tuple(map(int, line.split(",")))

    if section == 2:  # Nearby tickets
        tickets.append(tuple(map(int, line.split(","))))

valid_numbers = reduce(lambda a, b: a | b, rules.values(), set())
print(sum(0 if n in valid_numbers else n for t in tickets for n in t))

valid_tickets = filter(lambda a: all(map(lambda x: x in valid_numbers, a)), tickets)
valid_tickets = list(valid_tickets)

possible = {}
num_fields = len(valid_tickets[0])
assert num_fields == len(rules)
for rule_name, valid in rules.items():
    matching = [all(map(lambda x: x[n] in valid, valid_tickets)) for n in range(num_fields)]
    possible[rule_name] = matching


known = {}
solved = set()
work = True
while len(known) != num_fields:
    for f in range(num_fields):
        if f in known:
            continue

        choices = [name for name, valid in possible.items() if valid[f] and name not in solved]
        if len(choices) == 1:
            known[f] = choices[0]
            solved.add(choices[0])

result = 1
for f, name in known.items():
    if name.startswith("departure"):
        result *= my_ticket[f]
print(result)


from sys import stdin
from itertools import product

input = stdin.readlines()

# Part 1
masks = ()
mem = {}
for line in input:
    beg, value = line.split("=")
    if beg.startswith("mask"):
        zeroes = int(value.replace("X", "0"), 2)
        ones = int(value.replace("X", "1"), 2)
        masks = (zeroes, ones)
    else:
        n = int(value, 10)
        addr = int(beg.split("[")[1][:-2], 10)
        mem[addr] = (n & masks[1]) | masks[0]


print(sum(mem.values()))

# Part 2
def generate_masks(mask, n):
    min_addrs = int(mask.replace("X", "0"), 2) | n
    min_addrs &= int(mask.replace("0", "1").replace("X", "0"), 2)
    xs = mask.replace("1", "0")
    num_xs = xs.count("X")
    for res in product([0, 1], repeat=num_xs):
        wip = xs
        for n in res:
            wip = wip.replace("X", str(n), 1)
        value = int(wip, 2) | min_addrs
        yield value


mem = {}
for line in input:
    beg, value = line.split("=")
    if beg.startswith("mask"):
        masks = value
    else:
        value = int(value, 10)
        addr = int(beg.split("[")[1][:-2], 10)
        for a in generate_masks(masks, addr):
            mem[a] = value

print(sum(mem.values()))

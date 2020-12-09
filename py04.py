import sys


parsed = []
content = sys.stdin.read()
for group in content.split("\n\n"):
    parsed.append({x.split(":")[0]:x.split(":")[1] for x in group.split()})

expected = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # "cid"]
def valid1(x):
    return all(f in x for f in expected)
print(sum(valid1(x) for x in parsed))

def byr(x):
    try:
        return 1920 <= int(x) <= 2002
    except:
        return False

def iyr(x):
    try:
        return 2010 <= int(x) <= 2020
    except:
        return False

def eyr(x):
    try:
        return 2020 <= int(x) <= 2030
    except:
        return False

def hgt(x):
    n, kind = x[:-2], x[-2:]
    try:
        n = int(n)
    except:
        return False

    if kind == "cm":
        return 150 <= n <= 193
    elif kind == "in":
        return 59 <= n <= 76
    return False

def hcl(x):
    if x[0] != "#":
        return False
    valid = "0123456789abcdef"
    return sum(c in valid for c in x[1:]) == 6

def ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(x):
    try:
        int(x)
    except:
        return False
    return len(x) == 9

val = {
    "byr": byr, "iyr": iyr, "eyr": eyr,
    "hgt": hgt, "hcl": hcl, "ecl": ecl,
    "pid": pid,
}# "cid"]

def valid2(x):
    for k, f in val.items():
        if k not in x:
            return False
        if not f(x[k]):
            return False
    return True

print(sum(valid2(x) for x in parsed))

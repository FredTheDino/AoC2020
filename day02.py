def parse(line):
    a, b, c = line.split()
    return (*tuple(map(int, a.split("-"))),
            b[:1],
            c)


tests = []
while True:
    try:
        tests.append(parse(input()))
    except Exception as e:
        break


def valid1(low, hi, c, line):
    return low <= line.count(c) <= hi


print(sum(valid1(*t) for t in tests))


def valid2(low, hi, c, line):
    return (line[low-1] == c) != (line[hi-1] == c)


print(sum(valid2(*t) for t in tests))

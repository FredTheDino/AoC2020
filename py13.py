import sys
from itertools import count

depart, busses = [x for x in sys.stdin.readlines()]
depart = int(depart)
busses = [x for x in busses.split(",")]
wait_time = [(int(x) - depart % int(x), int(x)) for x in busses if x != "x"]
closest_depart = min(wait_time)
print(closest_depart[0] * closest_depart[1])

def best_buss_time(xs, start=0, step=1):
    if not xs:
        return start

    x, o = xs[0]
    for n in count(start, step):
        if -n % x == o % x:
            return best_buss_time(xs[1:], n, step * x)

busses = [(int(x), i) for i, x in enumerate(busses) if x != "x"]
print(best_buss_time(busses))

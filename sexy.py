from subprocess import run
from string import ascii_letters
from time import time
from math import log, floor


def run_as(cmd, stdin=None):
    out = run(cmd,
              input=stdin,
              encoding="utf-8",
              shell=True,
              capture_output=True)
    if out.returncode:
        print("Program failed:", *cmd)
        print(out.stderr)
        assert False
    return out.stdout


def find_all_inputs():
    return [day for day in run_as(["ls"]).split()
            if day.startswith("input")]


def find_all_days():
    return [int(i.strip("." + ascii_letters)) for i in find_all_inputs()]


def run_and_time_day(day, times=1):
    start = time()
    for _ in range(times):
        stdin = open(f"input{day:02}.txt").read()
        out = run_as([f"python3 py{day:02}.py"], stdin)
    end = time()
    taken = end - start
    average = taken / times
    p0, p1 = out.split("\n")[0:2]
    return day, taken, average, p0, p1


def run_and_time_all_days(times=1):
    for d in find_all_days():
        yield run_and_time_day(d, times)


def run_gu():
    out = run_as("cd gu/20/py/; python3 aoc20.py --no-decorate")
    result = dict()
    for line in out.split("\n"):
        if not line: continue
        day, t1, a, t2, b = line.split()
        result[int(day)] = (float(t1) + float(t2)) / 100.0, a, b
    return result


def setup_gu():
    run_as("cd gu; git stash; git pull --force;")
    run_as("mkdir -p gu/20/input/")
    for day in find_all_days():
        run_as(f"cp -f input{day:02}.txt gu/20/input/{day:02}")


def sexy_print(times=1):
    gu_res = run_gu()
    print("       -- AoC 2020 --")
    for day, _, avg, a, b in run_and_time_all_days(times):
        delta = ""
        if day in gu_res:
            gu_t, gu_a, gu_b = gu_res[day]
            if a == gu_a and b == gu_b:
                delta = floor(log(abs(avg - gu_t), 10))
                winner = "ed" if avg < gu_t else "gu"
            else:
                winner = "??"
        else:
            gu_t, gu_a, gu_b = 0, "", ""
            winner = "ed"

        print(f"{day:02} {winner:2<} ", end="")
        if delta:
            print(f"| E{delta:<2} |", end="")
        else:
            print(f"| --- |", end="")
        print(f"{a:>11} {b:<11}")

# setup_gu()
sexy_print(2)

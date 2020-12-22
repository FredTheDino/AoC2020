from subprocess import run
from string import ascii_letters
from time import time
from math import log, floor

# intrp = "pypy3"
intrp = "python3"

def run_as(cmd, stdin=None, can_fail=False):
    out = run(cmd,
              input=stdin,
              encoding="utf-8",
              shell=True,
              capture_output=True)
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
        out = run_as([f"{intrp} py{day:02}.py"], stdin)
    end = time()
    taken = end - start
    average = taken / times
    p0, p1 = out.split("\n")[0:2]
    return taken, average, p0, p1


def run_and_time_all_days(times=1):
    for d in find_all_days():
        yield run_and_time_day(d, times)


def run_and_time_gu_day(day, times=1):
    start = time()
    for _ in range(times):
        try:
            out = run_as([f"cd gu/20/py/; {intrp} d{day:02}.py"])
        except:
            return 0, 0, "", ""
    end = time()
    taken = end - start
    average = taken / times
    try:
        p0, p1 = out.split("\n")[0:2]
    except:
        p0, p1 = "", ""
    return taken, average, p0, p1

def run_all_gu(times=1):
    for d in find_all_days():
        yield run_and_time_gu_day(d, times)


def setup_gu():
    run_as(["cd gu; git stash; git pull --force;"])
    run_as(["mkdir -p gu/20/input/"])
    for day in find_all_days():
        run_as([f"cp -f input{day:02}.txt gu/20/input/{day:02}"])


def sexy_print(times=1):
    print(" = AoC 2020 =")
    wins = {"ed":0, "??":0, "gu": 0}
    longest = 0
    total_ed, total_gu = 0, 0
    for day, (_, gu_avg, gu_a, gu_b), (_, ed_avg, ed_a, ed_b) in zip(
        find_all_days(), run_all_gu(times), run_and_time_all_days(times)):

        total_ed += ed_avg
        total_gu += gu_avg

        delta = None
        if ed_a == gu_a and ed_b == gu_b:
            delta = round(abs(ed_avg - gu_avg), 4)
            winner = "ed" if ed_avg < gu_avg else "gu"
        else:
            winner = "??"

        line = f"{day:02} {winner:2<} "
        if delta:
            line += f"| {delta:<6} |"
        else:
            line += f"| ------ |"
        line += f"{ed_a:>15} {ed_b:<15}"
        print(line)
        longest = max(len(line), longest)
        wins[winner] += 1

    print("=" * longest)
    print(f"   ed: {wins['ed']:<7} gu: {wins['gu']:<7}")
    print(f"   ed: {round(total_ed, 3):<7} gu: {round(total_gu, 3):<7}")

if __name__ == "__main__":
    setup_gu()
    sexy_print(1)

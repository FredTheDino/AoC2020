import sys

prog = []
for line in sys.stdin.readlines():
    code, oper = line.split()
    prog.append((code, int(oper)))

def run_until_dup(prog):
    acc = 0
    ip = 0
    run = set()
    while True:
        if ip in run:
            return False, acc
        if ip == len(prog):
            return True, acc
        run.add(ip)
        code, oper = prog[ip]
        ip += 1
        if code == "nop":
            ...
        elif code == "acc":
            acc += oper
        elif code == "jmp":
            ip += oper - 1

print(run_until_dup(prog)[1])

def run_and_try_everything(prog):
    def all_mutations():
        for i, line in enumerate(prog):
            oldcode, oper = line
            if oldcode == "jmp":
                prog[i] = "nop", oper
                yield prog
            elif oldcode == "nop":
                prog[i] = "jmp", oper
                yield prog
            prog[i] = oldcode, oper

    for mut in all_mutations():
        success, acc = run_until_dup(mut)
        if success:
            return acc

print(run_and_try_everything(prog))

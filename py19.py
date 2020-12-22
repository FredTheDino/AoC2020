import sys

def parse_rule(line):
        n, rule = line.split(":")
        if "\"" in rule:
            return int(n), rule.strip("\" ")
        else:
            return int(n),  [list(map(int, r.split())) for r in rule.split("|")]

parsing_rules = True
rules = {}
queries = []
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        parsing_rules = False
        continue

    if parsing_rules:
        n, rule = parse_rule(line)
        rules[n] = rule
    else:
        queries.append(line)


def match(rules, rule, string, special=True):
    # EOF
    if not string:
        return False, ""

    # SIMPLE RULE
    rule = rules[rule]
    if isinstance(rule, str):
        return string[0] == rule, string[1:]

    # SUB RULE
    for alt in rule:
        string_copy = string
        for subrule in alt:
            is_match, string_copy = match(rules, subrule, string_copy, special)
            if not is_match:
                break
        else:
            return True, string_copy

    return False, ""

def is_match(rules, string):
    result = match(rules, 0, string)
    return result[0] and result[1] == ""

print(sum(is_match(rules, query) for query in queries))

def possible_rules(rules):
    for i in range(1, 10):
        for j in range(1, 10):
            rules[8] = [[42] * i]
            rules[11] = [[42] * j + [31] * j]
            yield rules


print(sum(any(is_match(alt, query) for alt in possible_rules(rules)) for query in queries))

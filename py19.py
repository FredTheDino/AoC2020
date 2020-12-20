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


def match(rules, rule, string, recurse=True):
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
            is_match, string_copy = match(rules, subrule, string_copy)
            if not is_match:
                break
        else:
            return True, string_copy

    return False, ""

def is_match(rules, string):
    result = match(rules, 0, string)
    return result[0] and result[1] == ""

#print(sum(is_match(rules, query) for query in queries))

for line in ["8: 42 8 | 42", "11: 42 11 31 | 42 31"]:
    n, rule = parse_rule(line)
    rules[n] = rule


for query in queries:
    if is_match(rules, query):
        print("MATCH", query)
    else:
        print("-----", query)

print(sum(is_match(rules, query) for query in queries))

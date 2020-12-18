import sys

def tokenize(line):
    return line.replace("(", "( ").replace(")", " )").split()


def eval1(line):
    def parse_value(tokens):
        t = tokens[0]
        if t == "(":
            tokens, value = eval_expr(tokens[1:])
            return tokens, value
        return tokens[1:], int(t)


    def eval_expr(tokens):
        tokens, value = parse_value(tokens)
        while tokens:
            t = tokens[0]
            if t == ")":
                return tokens[1:], value
            elif t in ["*", "+"]:
                oper = t
                tokens, other = parse_value(tokens[1:])
                if t == "*":
                    value *= other
                else:
                    value += other
        return tokens, value

    return eval_expr(tokenize(line))[1]


input = sys.stdin.readlines()

print(sum(eval1(line) for line in input))

def eval2(line):
    def parse_value(tokens):
        t = tokens[0]
        if t == "(":
            tokens, value = eval_expr(tokens[1:])
            return tokens[1:], value
        return tokens[1:], int(t)

    def eval_expr(tokens):
        tokens, value = parse_value(tokens)
        while tokens:
            t = tokens[0]
            if t == ")":
                return tokens, value
            elif t == "+":
                tokens, other = parse_value(tokens[1:])
                value += other
            elif t == "*":
                tokens, other = eval_expr(tokens[1:])
                value *= other

        return tokens, value

    return eval_expr(tokenize(line))[1]

print(sum(eval2(line) for line in input))

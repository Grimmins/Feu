import sys

def sum(a, b):
    return float(a) + float(b)


def diff(a, b):
    return float(a) - float(b)


def mul(a, b):
    return float(a) * float(b)


def div(a, b):
    if float(b) == 0:
        return "ERROR (div by zero)"
    return float(a) / float(b)


def mod(a, b):
    if float(b) == 0:
        return "ERROR (modulo by zero)"
    return float(a) % float(b)


def eval_expr(expr):
    start = -1
    end = -1
    expr = expr.replace(" ", "")
    for i in range(len(expr)):
        if expr[i] == "(":
            start = i
        elif expr[i] == ")":
            end = i
            break
    if start < end:
        sub_result = eval_expr(expr[start + 1:end])
        expr = expr[:start] + str(sub_result) + expr[end + 1:]
    for i in range(len(expr)):
        if expr[i] == "+":
            return sum(eval_expr(expr[:i]), eval_expr(expr[i + 1:]))
        elif expr[i] == "-":
            return diff(eval_expr(expr[:i]), eval_expr(expr[i + 1:]))
    for i in range(len(expr)):
        if expr[i] == "*":
            return mul(eval_expr(expr[:i]), eval_expr(expr[i + 1:]))
        elif expr[i] == "/":
            return div(eval_expr(expr[:i]), eval_expr(expr[i + 1:]))
        elif expr[i] == "%":
            return mod(eval_expr(expr[:i]), eval_expr(expr[i + 1:]))

    if expr == "":
        return 0

    return float(expr)

#
# expr = "4 + 21 * (1 - 2 / 2) + 38"
# expr = "4 + 21 * (17 - (4 * 7) / 2) + 38"
# print(eval_expr(expr))
#

print(eval_expr(sys.argv[1]))
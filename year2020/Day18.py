INPUT_FILE = "./year2020/data/day18.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def calc(nums, ops):
    op, n2, n1 = ops.pop(), nums.pop(), nums.pop()
    return n1 + n2 if op == "+" else n1 * n2


def precedence(x, prec_plus=1):
    return {"+": prec_plus, "*": 1, "(": 0}[x]


def evaluate(text, prec_plus=1):
    nums, ops = [], []
    for x in text.replace("(", "( ").replace(")", " )").split():
        if x.isnumeric():
            nums += [int(x)]
        elif x == "(":
            ops += [x]
        elif x == ")":
            while ops[-1] != "(":
                nums += [calc(nums, ops)]
            ops.pop()
        else:
            while ops and precedence(x, prec_plus) <= precedence(ops[-1], prec_plus):
                nums += [calc(nums, ops)]
            ops += [x]
    while ops:
        nums += [calc(nums, ops)]
    return nums.pop()


print(f"part 1: {sum(evaluate(line) for line in data)}")
print(f"part 2: {sum(evaluate(line, 2) for line in data)}")

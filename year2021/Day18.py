file = open("./year2021/data/day18.txt", "r")
lines = [line.rstrip('\n') for line in file]


def split(x):
    for i in range(len(x)):
        if type(x[i]) == int and x[i] >= 10:
            return x[:i] + ["[", (x[i] // 2), ",", ((x[i] + 1) // 2), "]"] + x[i + 1:], True
    return x, False


def add_right(x, to_add):
    for i in range(len(x) - 1, -1, -1):
        if type(x[i]) == int:
            return x[:i] + [x[i] + to_add] + x[i + 1:]
    return x


def add_left(x, to_add):
    for i in range(len(x)):
        if type(x[i]) == int:
            return x[:i] + [x[i] + to_add] + x[i + 1:]
    return x


def explode(x):
    depth = 0
    for i in range(len(x)):
        depth += (1 if x[i] == "[" else (-1 if x[i] == "]" else 0))
        if depth == 5:
            return add_right(x[:i], x[i + 1]) + [0] + add_left(x[i + 5:], x[i + 3]), True
    return x, False


def reduce(x):
    while True:
        x, has_exploded = explode(x)
        if not has_exploded:
            x, has_slpit = split(x)
            if not has_slpit:
                break
    return x


def add(x, y):
    return reduce(["["] + x + [","] + y + ["]"])


def magnitude(x):
    stack = []
    for e in x:
        if type(e) == int:
            stack.append(e)
        elif e == "]":
            stack.append(2 * stack.pop() + 3 * stack.pop())  # reverse order on stack!
    return stack.pop()


numbers = [[(int(c) if c.isdigit() else c) for c in line] for line in lines]

sum_numbers = numbers[0]
for i in range(1, len(numbers)):
    sum_numbers = add(sum_numbers, numbers[i])
print(magnitude(sum_numbers))

best_magnitude = 0
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        best_magnitude = max(best_magnitude, magnitude(add(numbers[i], numbers[j])))
        best_magnitude = max(best_magnitude, magnitude(add(numbers[j], numbers[i])))
print(best_magnitude)

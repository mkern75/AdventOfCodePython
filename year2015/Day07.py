from collections import defaultdict

file = open("./year2015/data/day07.txt", "r")
lines = [line.rstrip('\n') for line in file]


def val(x, solution):
    return int(x) if x.isnumeric() else (solution[x] if x in solution else None)


def solve(todo):
    solution = defaultdict(int)
    while len(todo) > 0:
        remain = []
        for line in todo:
            before, after = line.split(" -> ")
            x = before.split()
            if len(x) == 1:
                if val(x[0], solution) is not None:
                    solution[after] = val(x[0], solution)
                else:
                    remain.append(line)
            else:
                if x[0] == "NOT":
                    if val(x[1], solution) is not None:
                        solution[after] = 65535 - val(x[1], solution)
                    else:
                        remain.append(line)
                else:
                    if val(x[0], solution) is None or val(x[2], solution) is None:
                        remain.append(line)
                    elif x[1] == "AND":
                        solution[after] = val(x[0], solution) & val(x[2], solution)
                    elif x[1] == "OR":
                        solution[after] = val(x[0], solution) | val(x[2], solution)
                    elif x[1] == "LSHIFT":
                        solution[after] = val(x[0], solution) << val(x[2], solution)
                    elif x[1] == "RSHIFT":
                        solution[after] = val(x[0], solution) >> val(x[2], solution)
        todo = remain
    return solution


a = solve(lines)["a"]
print(a)

todo = [line for line in lines if not line.endswith(" -> b")]
todo.append(str(a) + " -> b")
print(solve(todo)["a"])

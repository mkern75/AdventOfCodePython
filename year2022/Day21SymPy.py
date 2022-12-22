import sympy

INPUT_FILE = "./year2022/data/day21.txt"

OP = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

# part 1
jobs = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
val = {}
while True:
    jobs_left = []
    for job in jobs:
        monkey, other = job.split(": ")
        if other.isnumeric():
            val[monkey] = sympy.Integer(other)
        else:
            monkey1, op, monkey2 = other.split()
            if monkey1 in val and monkey2 in val:
                val[monkey] = OP[op](val[monkey1], val[monkey2])
            else:
                jobs_left += [job]
    if len(jobs) == len(jobs_left):
        break
    jobs = jobs_left
print(f"part 1: {val['root']}")

# part 2
jobs = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
val = {}
while True:
    jobs_left = []
    for job in jobs:
        monkey, other = job.split(": ")
        if other.isnumeric():
            if monkey == "humn":
                val[monkey] = sympy.Symbol("x")
            else:
                val[monkey] = sympy.Integer(other)
        else:
            monkey1, op, monkey2 = other.split()
            if monkey1 in val and monkey2 in val:
                if monkey == "root":
                    print(f"part 2: {sympy.solve(val[monkey1] - val[monkey2])[0]}")
                else:
                    val[monkey] = OP[op](val[monkey1], val[monkey2])
            else:
                jobs_left += [job]
    if len(jobs) == len(jobs_left):
        break
    jobs = jobs_left

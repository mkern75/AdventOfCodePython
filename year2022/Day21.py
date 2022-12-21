INPUT_FILE = "./year2022/data/day21.txt"
jobs = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def calc(goal, jobs):
    values = {}
    while True:
        jobs_left = []
        for job in jobs:
            monkey, other = job.split(": ")
            if other.isnumeric():
                values[monkey] = int(other)
            else:
                monkey1, op, monkey2 = other.split()
                if op == "=" and monkey1 in values:
                    values[monkey2] = values[monkey1]
                elif op == "=" and monkey2 in values:
                    values[monkey1] = values[monkey2]
                elif monkey1 in values and monkey2 in values:
                    if op == "+":
                        values[monkey] = values[monkey1] + values[monkey2]
                    elif op == "-":
                        values[monkey] = values[monkey1] - values[monkey2]
                    elif op == "*":
                        values[monkey] = values[monkey1] * values[monkey2]
                    elif op == "/":
                        values[monkey] = values[monkey1] // values[monkey2]
                elif monkey in values and monkey1 in values:
                    if op == "+":
                        values[monkey2] = values[monkey] - values[monkey1]
                    elif op == "-":
                        values[monkey2] = values[monkey1] - values[monkey]
                    elif op == "*":
                        values[monkey2] = values[monkey] // values[monkey1]
                    elif op == "/":
                        values[monkey2] = values[monkey1] // values[monkey]
                elif monkey in values and monkey2 in values:
                    if op == "+":
                        values[monkey1] = values[monkey] - values[monkey2]
                    elif op == "-":
                        values[monkey1] = values[monkey] + values[monkey2]
                    elif op == "*":
                        values[monkey1] = values[monkey] // values[monkey2]
                    elif op == "/":
                        values[monkey1] = values[monkey] * values[monkey2]
                else:
                    jobs_left += [job]
        if goal in values:
            return values[goal]
        if len(jobs_left) == 0 or len(jobs_left) == len(jobs):
            return None
        jobs = jobs_left


# part 1
ans1 = calc("root", jobs)
print(f"part 1: {ans1}")

# part 2
you = next(job for job in jobs if job.startswith("humn:"))
jobs.remove(you)
root = next(job for job in jobs if job.startswith("root:"))
jobs.remove(root)
jobs.insert(0, root.replace("+", "=").replace("-", "=").replace("*", "=").replace("/", "="))
ans2 = calc("humn", jobs)
print(f"part 2: {ans2}")

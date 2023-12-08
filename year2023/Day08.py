import math

INPUT_FILE = "./year2023/data/day08.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

instructions = list(data[0])
N = len(instructions)

network = {}
for line in data[2:]:
    src, dest = line.split(" = ")
    network[src] = tuple(dest.replace("(", "").replace(")", "").split(", "))


def calc_n_steps(start, goal_ends_with):
    curr, i = start, 0
    while not curr.endswith(goal_ends_with):
        curr = network[curr][0] if instructions[i % N] == "L" else network[curr][1]
        i += 1
    return i


ans1 = calc_n_steps("AAA", "ZZZ")
# part 2 only works this way because of the special structure of the input; general case is much harder
ans2 = math.lcm(*[calc_n_steps(x, "Z") for x in network.keys() if x.endswith("A")])

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

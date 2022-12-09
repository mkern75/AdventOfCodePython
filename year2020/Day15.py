INPUT_FILE = "./year2020/data/day15.txt"
data = [int(x) for line in open(INPUT_FILE, "r") for x in line.rstrip('\n').split(",")]


def solve(max_cycle):
    n, cycle_last, cycle_before = 0, {}, {}
    for c in range(max_cycle):
        if c < len(data):
            n = data[c]
        else:
            n = 0 if n not in cycle_before else cycle_last[n] - cycle_before[n]
        if n in cycle_last:
            cycle_before[n] = cycle_last[n]
        cycle_last[n] = c
    return n


print(f"part 1: {solve(2020)}")
print(f"part 2: {solve(30000000)}")

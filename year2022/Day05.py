from collections import defaultdict
import re

INPUT_FILE = "./year2022/data/day05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
split = data.index("")
data_start, data_proc = data[:split], data[split + 1:]


def load_start_stacks(data_start):
    stacks = defaultdict(list)
    for line in data_start[:-1][::-1]:  # ignore last line with stack numbers; reverse order to build stacks bottom up
        for i in range(0, len(line), 4):
            if line[i] == "[":
                stacks[i // 4 + 1] += [line[i + 1]]
    return stacks


def rearrange_stacks(stacks, data_proc, reverse):
    for line in data_proc:
        n, fr, to = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
        if reverse:
            stacks[to].extend(stacks[fr][-n:][::-1])  # part 1
        else:
            stacks[to].extend(stacks[fr][-n:])  # part 2
        stacks[fr] = stacks[fr][:-n]
    return stacks


# part 1
stacks = load_start_stacks(data_start)
stacks = rearrange_stacks(stacks, data_proc, True)
ans1 = "".join(stacks[i + 1][-1] for i in range(max(stacks)))
print(f"part 1: {ans1}")

# part 2
stacks = load_start_stacks(data_start)
stacks = rearrange_stacks(stacks, data_proc, False)
ans2 = "".join(stacks[i + 1][-1] for i in range(max(stacks)))
print(f"part 2: {ans2}")

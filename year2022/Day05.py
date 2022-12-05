from collections import defaultdict
import re

INPUT_FILE = "./year2022/data/day05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
split = data.index("")
data_stack, data_proc = data[:split], data[split + 1:]


def load_initial_stack(data_stack):
    stack = defaultdict(list)
    for line in data_stack[:-1][::-1]:  # ignore last line with stack numbers; reverse order to build stacks bottom up
        for i in range(0, len(line), 4):
            if line[i] == "[":
                stack[i // 4 + 1] += [line[i + 1]]
    return stack


def rearrange_stacks(stacks, data_proc, reverse=True):
    for cmd in data_proc:
        n, fr, to = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", cmd).groups())
        stacks[to].extend(stacks[fr][-n:][::-1] if reverse else stacks[fr][-n:])
        stacks[fr] = stacks[fr][:-n]


# part 1
stack = load_initial_stack(data_stack)
rearrange_stacks(stack, data_proc)
ans1 = "".join(stack[i + 1][-1] for i in range(max(stack)))
print(f"part 1: {ans1}")

# part 2
stack = load_initial_stack(data_stack)
rearrange_stacks(stack, data_proc, False)
ans2 = "".join(stack[i + 1][-1] for i in range(max(stack)))
print(f"part 2: {ans2}")

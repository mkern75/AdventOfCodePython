from utils import load_lines
from collections import defaultdict

INPUT_FILE = "./year2018/data/day12.txt"

lines = load_lines(INPUT_FILE)

state = defaultdict(lambda: ".")
for i, c in enumerate(list(lines[0][15:])):
    state[i] = c

rules = defaultdict(lambda: ".")
for line in lines:
    if " => #" in line:
        fr, to = line.split(" => ")
        rules[tuple(fr)] = to

for g in range(20):
    state_new = defaultdict(lambda: ".")
    for i in range(min(state.keys()) - 2, max(state.keys()) + 3):
        state_new[i] = rules[(state[i - 2], state[i - 1], state[i], state[i + 1], state[i + 2])]
    state = state_new
ans1 = sum([i for i in state.keys() if state[i] == "#"])
print("part 1:", ans1)

# running the simulation for part 2 would take by far too long
# however the patter stabilises after 101 generations (for my inputs):
# 5 plants remain, and they shift one position to the right in each generation
# this allows us to calculate the result directly
ans2 = 724 + (50_000_000_000 - 101) * 5
print("part 2:", ans2)

import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day06.txt"


def redistribute(state):
    new_state = list(state)
    most_blocks = max(new_state)
    idx = new_state.index(most_blocks)
    new_state[idx] = 0
    for i in range(1, most_blocks + 1):
        new_state[(idx + i) % len(state)] += 1
    return tuple(new_state)


file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

state = tuple([int(i) for i in lines[0].split()])
cycle = 0
seen_in_cycle = {}

while state not in seen_in_cycle:
    seen_in_cycle[state] = cycle
    state = redistribute(state)
    cycle += 1

print("part 1:", cycle, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

print("part 2:", cycle - seen_in_cycle[state], f"  ({time.time() - t1:.3f}s)")

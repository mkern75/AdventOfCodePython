import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day05.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

instructions = [int(line) for line in lines]
i, steps = 0, 0
while 0 <= i < len(instructions):
    i_next = i + instructions[i]
    instructions[i] += 1
    i = i_next
    steps += 1
print("part 1:", steps, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

instructions = [int(line) for line in lines]
i, steps = 0, 0
while 0 <= i < len(instructions):
    i_next = i + instructions[i]
    instructions[i] += -1 if instructions[i] >= 3 else +1
    i = i_next
    steps += 1
print("part 2:", steps, f"  ({time.time() - t1:.3f}s)")

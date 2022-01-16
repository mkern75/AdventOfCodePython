from utils import load_numbers, tic, toc

INPUT_FILE = "./year2017/data/day05.txt"

tic()
instructions = load_numbers(INPUT_FILE)
i, steps = 0, 0
while 0 <= i < len(instructions):
    i_next = i + instructions[i]
    instructions[i] += 1
    i = i_next
    steps += 1
print(f"part 1: {steps}  ({toc():.3f}s)")

tic()
instructions = load_numbers(INPUT_FILE)
i, steps = 0, 0
while 0 <= i < len(instructions):
    i_next = i + instructions[i]
    instructions[i] += -1 if instructions[i] >= 3 else +1
    i = i_next
    steps += 1
print(f"part 2: {steps}  ({toc():.3f}s)")

from utils import load_int_program
from collections import defaultdict
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day19.txt"

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)


def check(x, y):
    computer.reset(program)
    computer.add_input(x)
    computer.add_input(y)
    computer.run()
    return computer.pop_output()


res1 = sum(check(x, y) for x in range(50) for y in range(50))
print("part 1:", res1)

s = 100
x, y_min, y_max = 10, defaultdict(lambda: 0), defaultdict(lambda: 0)
while True:
    x += 1
    y_min[x] = y_min[x - 1]
    while not check(x, y_min[x]):
        y_min[x] += 1
    y_max[x] = max(y_max[x - 1], y_min[x])
    while check(x, y_max[x] + 1):
        y_max[x] += 1
    if y_min[x] + (s - 1) <= y_max[x]:
        if y_min[x - (s - 1)] <= y_min[x] <= y_min[x] + (s - 1) <= y_max[x - (s - 1)]:
            res2 = 10000 * (x - (s - 1)) + y_min[x]
            break
print("part 2:", res2)

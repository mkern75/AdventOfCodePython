from utils import load_int_program
from IntcodeComputer import IntcodeComputer
from collections import defaultdict
from colorama import Back, Style

INPUT_FILE = "./year2019/data/day11.txt"


def paint(computer, start_on_white=False):
    grid = defaultdict(int)
    if start_on_white:
        grid[(0, 0)] = 1
    painted = set()
    x, y, dx, dy, step = 0, 0, 0, 1, 0
    while True:
        step += 1
        computer.add_input(grid[(x, y)])
        computer.run()
        if not computer.has_output():
            break
        grid[(x, y)] = computer.pop_output()
        painted.add((x, y))
        if computer.pop_output() == 0:
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
    return grid, painted


def display_grid(grid):
    x_min, x_max = min([x for (x, _) in grid.keys()]), max([x for (x, _) in grid.keys()])
    y_min, y_max = min([y for (_, y) in grid.keys()]), max([y for (_, y) in grid.keys()])
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1, 1):
            if grid[(x, y)] == 1:
                print(Back.GREEN + "#" + Style.RESET_ALL, end="")
            else:
                print(".", end="")
        print()


program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)
_, painted = paint(computer)
print("part 1:", len(painted))

computer.reset(program)
grid, _ = paint(computer, True)
print("part2:")
display_grid(grid)

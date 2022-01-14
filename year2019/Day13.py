from utils import load_int_program, sgn
from IntcodeComputer import IntcodeComputer
from colorama import Fore, Back, Style
import time

INPUT_FILE = "./year2019/data/day13.txt"
SHOW_ARCADE = False


def update_grid_and_score(grid, score, computer):
    refresh = False
    while computer.has_output(3):
        x, y, v = computer.pop_output(), computer.pop_output(), computer.pop_output()
        if x == -1 and y == 0:
            score = v
        else:
            grid[(x, y)] = v
        if v in [3, 4]:
            refresh = True
    return grid, score, refresh


def display(screen, score):
    r_max, c_max = max([y for (_, y) in screen.keys()]), max([x for (x, _) in screen.keys()])
    for r in range(r_max + 1):
        for c in range(c_max + 1):
            if screen[(c, r)] == 0:
                print(" ", end="")
            elif screen[(c, r)] == 1:
                print("#", end="")
            elif screen[(c, r)] == 2:
                print(Fore.GREEN + "+" + Style.RESET_ALL, end="")
            elif screen[(c, r)] == 3:
                print(Back.GREEN + "-" + Style.RESET_ALL, end="")
            elif screen[(c, r)] == 4:
                print(Back.RED + "o" + Style.RESET_ALL, end="")
        print()
    print("score:", score)
    print()


program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)
computer.run()
grid = {}
score = 0
grid, score, _ = update_grid_and_score(grid, score, computer)
if SHOW_ARCADE:
    display(grid, score)
print("part 1:", sum([1 for v in grid.values() if v == 2]))

computer.reset(program)
computer.set_memory(0, 2)

while not computer.is_finished():
    if computer.has_output(3):
        grid, score, refresh = update_grid_and_score(grid, score, computer)
        if SHOW_ARCADE and refresh:
            display(grid, score)
            time.sleep(0.01)
    computer.run_one_cycle()
    if computer.is_awating_input():
        x_ball, _ = list(grid.keys())[list(grid.values()).index(4)]
        x_paddle, _ = list(grid.keys())[list(grid.values()).index(3)]
        computer.add_input(sgn(x_ball - x_paddle))

print("part 2:", score)

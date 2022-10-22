from utils import load_int_program
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day23.txt"

program = load_int_program(INPUT_FILE)


def setup_computers():
    computer = []
    for i in range(50):
        computer += [IntcodeComputer(program)]
        computer[i].add_input(i)
        computer[i].run()
    return computer


def run(computer):
    if not computer.has_input():
        computer.add_input(-1)
    computer.run()
    return (computer.pop_output(), computer.pop_output(), computer.pop_output()) if computer.has_output() else None


def run_part1():
    computers = setup_computers()
    while True:
        for i in range(50):
            if output := run(computers[i]):
                addr, x, y = output
                if addr == 255:
                    return y
                else:
                    computers[addr].add_input(x)
                    computers[addr].add_input(y)


def run_part2():
    computers = setup_computers()
    nat_x, nat_y, y_prev = None, None, None
    while True:
        inactive = True
        for i in range(50):
            if output := run(computers[i]):
                addr, x, y = output
                inactive = False
                if addr == 255:
                    nat_x, nat_y = x, y
                else:
                    computers[addr].add_input(x)
                    computers[addr].add_input(y)
        if inactive:
            if nat_y == y_prev:
                return nat_y
            computers[0].add_input(nat_x)
            computers[0].add_input(nat_y)
            y_prev = nat_y


print("part 1:", run_part1())
print("part 2:", run_part2())

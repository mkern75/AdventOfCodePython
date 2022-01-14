from utils import load_int_program
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day02.txt"

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)
computer.set_memory(1, 12)
computer.set_memory(2, 2)
computer.run()
print("part 1:", computer.get_memory(0))

ans2 = -1
for noun in range(100):
    for verb in range(100):
        computer.reset(program)
        computer.set_memory(1, noun)
        computer.set_memory(2, verb)
        computer.run()
        if computer.get_memory(0) == 19690720:
            ans2 = 100 * noun + verb
print("part 2:", ans2)

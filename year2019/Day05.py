from utils import load_int_program
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day05.txt"

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)
computer.input += [1]
computer.run()
print("part 1:", computer.output[-1])

computer = IntcodeComputer(program)
computer.input += [5]
computer.run()
print("part 2:", computer.output[-1])

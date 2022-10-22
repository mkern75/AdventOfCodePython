from utils import load_int_program
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day21.txt"

program = load_int_program(INPUT_FILE)

# part 1: ~(A AND B AND C) AND D
computer = IntcodeComputer(program)
computer.add_ascii_input("NOT T T\n")
computer.add_ascii_input("AND A T\n")
computer.add_ascii_input("AND B T\n")
computer.add_ascii_input("AND C T\n")
computer.add_ascii_input("NOT T T\n")
computer.add_ascii_input("AND D T\n")
computer.add_ascii_input("OR T J\n")
computer.add_ascii_input("WALK\n")
computer.run()
print("part 1:", computer.pop_last_output())

# part 2: ~(A AND B AND C) AND D AND (E OR H)
computer = IntcodeComputer(program)
computer.add_ascii_input("NOT T T\n")
computer.add_ascii_input("AND A T\n")
computer.add_ascii_input("AND B T\n")
computer.add_ascii_input("AND C T\n")
computer.add_ascii_input("NOT T T\n")
computer.add_ascii_input("AND D T\n")
computer.add_ascii_input("OR E J\n")
computer.add_ascii_input("OR H J\n")
computer.add_ascii_input("AND T J\n")
computer.add_ascii_input("RUN\n")
computer.run()
print("part 2:", computer.pop_last_output())

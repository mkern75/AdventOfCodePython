from datetime import datetime
from MonorailComputer import MonorailComputer

INPUT_FILE = "./year2016/data/day23.txt"

print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
program = [line.rstrip('\n') for line in file]

computer = MonorailComputer(program)
computer.memory["a"] = 7
computer.run()
print("part 1:", computer.memory["a"])

computer.reset(program)
computer.memory["a"] = 12
computer.run()
print("part 2:", computer.memory["a"])

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

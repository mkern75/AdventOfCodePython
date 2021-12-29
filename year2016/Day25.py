from datetime import datetime
from MonorailComputer import MonorailComputer

INPUT_FILE = "./year2016/data/day25.txt"

print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
program = [line.rstrip('\n') for line in file]

computer = MonorailComputer(program)
n = 0
while True:
    n += 1
    computer.reset(program)
    computer.memory["a"] = n
    for i in range(100000):
        computer.run_one_instruction()
    check = True
    if len(computer.output) <= 5:
        check = False
    for i in range(len(computer.output)):
        if computer.output[i] != i % 2:
            check = False
    if check:
        print("part 1:", n)
        break

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

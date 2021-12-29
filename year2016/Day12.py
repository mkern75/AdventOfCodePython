from MonorailComputer import MonorailComputer

file = open("./year2016/data/day12.txt", "r")
program = [line.rstrip('\n') for line in file]

computer = MonorailComputer(program)
computer.run()
print("part 1:", computer.memory["a"])

computer.reset(program)
computer.memory["c"] = 1
computer.run()
print("part 2:", computer.memory["a"])

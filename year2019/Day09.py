from IntcodeComputer import IntcodeComputer

file = open("./year2019/data/day09.txt", "r")
lines = [line.rstrip('\n') for line in file]

program = list(map(int, lines[0].split(",")))

computer = IntcodeComputer(program)
computer.input += [1]
computer.run()
print("part 1:", computer.output[-1])

computer.reset(program)
computer.input += [2]
computer.run()
print("part 2:", computer.output[-1])

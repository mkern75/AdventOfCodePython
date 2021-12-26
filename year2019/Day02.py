from IntcodeComputer import IntcodeComputer

file = open("./year2019/data/day02.txt", "r")
lines = [line.rstrip('\n') for line in file]

program = list(map(int, lines[0].split(",")))

computer = IntcodeComputer(program)
computer.memory[1] = 12
computer.memory[2] = 2
computer.run()
print("part 1:", computer.memory[0])

ans2 = -1
for noun in range(100):
    for verb in range(100):
        computer.reset(program)
        computer.memory[1] = noun
        computer.memory[2] = verb
        computer.run()
        if computer.memory[0] == 19690720:
            ans2 = 100 * noun + verb
print("part 2:", ans2)

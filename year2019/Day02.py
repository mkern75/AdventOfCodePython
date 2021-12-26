from collections import defaultdict

file = open("./year2019/data/day02.txt", "r")
lines = [line.rstrip('\n') for line in file]


def run(program):
    mem = defaultdict()
    for i in range(len(program)):
        mem[i] = program[i]
    ip = 0
    while ip in mem:
        match mem[ip]:
            case 1:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] + mem[mem[ip + 2]]
                ip += 4
            case 2:
                mem[mem[ip + 3]] = mem[mem[ip + 1]] * mem[mem[ip + 2]]
                ip += 4
            case 99:
                break
    return mem


program = list(map(int, lines[0].split(",")))
program[1] = 12
program[2] = 2

ans1 = run(program)[0]
print("part 1:", ans1)

ans2 = 0
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        if run(program)[0] == 19690720:
            ans2 = 100 * noun + verb
print("part 2:", ans2)

from collections import defaultdict

file = open("./year2019/data/day05.txt", "r")
lines = [line.rstrip('\n') for line in file]


def get_value(pmode, i, ip, mem):
    while i > 1:
        pmode //= 10
        i -= 1
    if pmode % 10 == 0:
        return mem[mem[ip]]
    elif pmode % 10 == 1:
        return mem[ip]
    else:
        assert False, "wrong parameter mode"


def run(program, inp):
    mem = defaultdict()
    outp = []
    for i in range(len(program)):
        mem[i] = program[i]
    ip, inpp = 0, 0
    while ip in mem:
        opcode, pmode = mem[ip] % 100, mem[ip] // 100
        match opcode:
            case 1:  # add
                mem[mem[ip + 3]] = get_value(pmode, 1, ip + 1, mem) + get_value(pmode, 2, ip + 2, mem)
                ip += 4
            case 2:  # multiply
                mem[mem[ip + 3]] = get_value(pmode, 1, ip + 1, mem) * get_value(pmode, 2, ip + 2, mem)
                ip += 4
            case 3:  # input
                mem[mem[ip + 1]] = inp[inpp]
                inpp += 1
                ip += 2
            case 4:  # output
                outp += [get_value(pmode, 1, ip + 1, mem)]
                ip += 2
            case 5:  # jump-if-true
                if get_value(pmode, 1, ip + 1, mem) != 0:
                    ip = get_value(pmode, 2, ip + 2, mem)
                else:
                    ip += 3
            case 6:  # jump-if-false
                if get_value(pmode, 1, ip + 1, mem) == 0:
                    ip = get_value(pmode, 2, ip + 2, mem)
                else:
                    ip += 3
            case 7:  # less than
                if get_value(pmode, 1, ip + 1, mem) < get_value(pmode, 2, ip + 2, mem):
                    mem[mem[ip + 3]] = 1
                else:
                    mem[mem[ip + 3]] = 0
                ip += 4
            case 8:  # equals
                if get_value(pmode, 1, ip + 1, mem) == get_value(pmode, 2, ip + 2, mem):
                    mem[mem[ip + 3]] = 1
                else:
                    mem[mem[ip + 3]] = 0
                ip += 4
            case 99:
                break
    return mem, outp


program = list(map(int, lines[0].split(",")))
mem, outp = run(program, [1])
print("part 1:", outp[-1])

mem, outp = run(program, [5])
print("part 2:", outp[-1])


INPUT_FILE = "./year2020/data/day08.txt"
program = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def run(code):
    acc, ip, executed = 0, 0, set()
    while ip not in executed and 0 <= ip < len(code):
        executed |= {ip}
        if code[ip].startswith("acc"):
            acc += int(code[ip][4:])
            ip += 1
        elif code[ip].startswith("nop"):
            ip += 1
        else:
            ip += int(code[ip][4:])
    return acc, ip not in executed


print(f"part 1: {run(program)[0]}")

for i in range(len(program)):
    program_modified = [instr for instr in program]
    if program_modified[i].startswith("nop"):
        program_modified[i] = "jmp" + program_modified[i][3:]
    elif program[i].startswith("jmp"):
        program_modified[i] = "nop" + program_modified[i][3:]
    else:
        continue
    res, terminates = run(program_modified)
    if terminates:
        print(f"part 2: {res}")
        break

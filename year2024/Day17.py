from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day17.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]

register = {line[9]: int(line[12:]) for line in blocks[0]}
program = list(map(int, blocks[1][0][9:].split(",")))


def run(program, register):
    ip = 0
    out = []

    while ip < len(program) - 1:
        instr = program[ip]
        operand = program[ip + 1]

        literal = operand
        combo = 0
        if 0 <= operand <= 3:
            combo = operand
        elif operand == 4:
            combo = register["A"]
        elif operand == 5:
            combo = register["B"]
        elif operand == 6:
            combo = register["C"]

        if instr == 0:
            register["A"] = register["A"] >> combo
            ip += 2
        elif instr == 1:
            register["B"] = register["B"] ^ literal
            ip += 2
        elif instr == 2:
            register["B"] = combo % 8
            ip += 2
        elif instr == 3:
            ip = literal if register["A"] != 0 else ip + 2
        elif instr == 4:
            register["B"] = register["B"] ^ register["C"]
            ip += 2
        elif instr == 5:
            out += [combo % 8]
            ip += 2
        elif instr == 6:
            register["B"] = register["A"] >> combo
            ip += 2
        elif instr == 7:
            register["C"] = register["A"] >> combo
            ip += 2

    return out


output1 = run(program, register.copy())
ans1 = ",".join(map(str, output1))
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")


def solve(reg_a_val, pos):
    """This works for my inputs, not necessarily for others."""
    target = program[pos]
    for v in range(8):
        register_tmp = register.copy()
        register_tmp["A"] = reg_a_val | v
        out = run(program, register_tmp)
        if out[0] == target:
            if pos == 0:
                return reg_a_val | v
            else:
                res = solve((reg_a_val | v) << 3, pos - 1)
                if res is not None:
                    return res
    return None


ans2 = solve(0, len(program) - 1)
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

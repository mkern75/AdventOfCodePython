import time
from collections import defaultdict, namedtuple

t0 = time.time()
INPUT_FILE = "./year2017/data/day08.txt"

Instruction = namedtuple("Instruction", ["reg", "op", "val", "if_reg", "if_comp", "if_val"])


def load_instructions(filename):
    instructions = []
    lines = [line.rstrip('\n') for line in open(filename, "r")]
    for line in lines:
        s = line.split()
        instructions += [Instruction(s[0], s[1], int(s[2]), s[4], s[5], int(s[6]))]
    return instructions


def process(instructions):
    reg, highest_value = defaultdict(int), 0
    for instr in instructions:
        if (instr.if_comp == "==" and reg[instr.if_reg] == instr.if_val) or \
                (instr.if_comp == "!=" and reg[instr.if_reg] != instr.if_val) or \
                (instr.if_comp == ">=" and reg[instr.if_reg] >= instr.if_val) or \
                (instr.if_comp == "<=" and reg[instr.if_reg] <= instr.if_val) or \
                (instr.if_comp == ">" and reg[instr.if_reg] > instr.if_val) or \
                (instr.if_comp == "<" and reg[instr.if_reg] < instr.if_val):
            reg[instr.reg] += instr.val if instr.op == "inc" else -instr.val
        highest_value = max(highest_value, max(reg.values()))
    return reg, highest_value


instructions = load_instructions(INPUT_FILE)
registers, highest_value = process(instructions)

ans1 = max(registers.values())
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = highest_value
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

from utils import load_text_blocks

INPUT_FILE = "./year2018/data/day16.txt"

OPS = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr",
       "eqir", "eqri", "eqrr"]


def execute(op, a, b, c, registers):
    if op == "addr":
        registers[c] = registers[a] + registers[b]
    elif op == "addi":
        registers[c] = registers[a] + b
    elif op == "mulr":
        registers[c] = registers[a] * registers[b]
    elif op == "muli":
        registers[c] = registers[a] * b
    elif op == "banr":
        registers[c] = registers[a] & registers[b]
    elif op == "bani":
        registers[c] = registers[a] & b
    elif op == "borr":
        registers[c] = registers[a] | registers[b]
    elif op == "bori":
        registers[c] = registers[a] | b
    elif op == "setr":
        registers[c] = registers[a]
    elif op == "seti":
        registers[c] = a
    elif op == "gtir":
        registers[c] = 1 if a > registers[b] else 0
    elif op == "gtri":
        registers[c] = 1 if registers[a] > b else 0
    elif op == "gtrr":
        registers[c] = 1 if registers[a] > registers[b] else 0
    elif op == "eqir":
        registers[c] = 1 if a == registers[b] else 0
    elif op == "eqri":
        registers[c] = 1 if registers[a] == b else 0
    elif op == "eqrr":
        registers[c] = 1 if registers[a] == registers[b] else 0
    else:
        assert False


def possible_ops(instruction, registers_before, registers_after):
    ops = []
    a, b, c = instruction[1], instruction[2], instruction[3]
    for op in OPS:
        registers = registers_before.copy()
        execute(op, a, b, c, registers)
        if all([True if registers[i] == registers_after[i] else False for i in range(4)]):
            ops += [op]
    return ops


def map_opscodes(text_blocks):
    candidates = {}
    for i in range(len(text_blocks) - 1):
        registers_before = list(map(int, text_blocks[i][0][9:-1].split(",")))
        instruction = list(map(int, text_blocks[i][1].split()))
        registers_after = list(map(int, text_blocks[i][2][9:-1].split(",")))
        opscode = instruction[0]
        ops = set(possible_ops(instruction, registers_before, registers_after))
        if opscode in candidates:
            candidates[opscode] = (candidates[opscode].intersection(ops))
        else:
            candidates[opscode] = ops

    stop = False
    while not stop:
        stop = True
        for opcode, ops in candidates.items():
            if len(ops) == 1:
                op = list(ops)[0]
                for other_opcode in candidates.keys():
                    if other_opcode != opcode and op in candidates[other_opcode]:
                        candidates[other_opcode].remove(op)
                        stop = False

    opscode_map = {}
    for opscode, ops in candidates.items():
        opscode_map[opscode] = list(ops)[0]

    return opscode_map


text_blocks = load_text_blocks(INPUT_FILE)

ans1 = 0
for i in range(len(text_blocks) - 1):
    registers_before = list(map(int, text_blocks[i][0][9:-1].split(",")))
    instruction = list(map(int, text_blocks[i][1].split()))
    registers_after = list(map(int, text_blocks[i][2][9:-1].split(",")))
    if len(possible_ops(instruction, registers_before, registers_after)) >= 3:
        ans1 += 1
print("part 1:", ans1)

opscode_map = map_opscodes(text_blocks)
reg = [0, 0, 0, 0]
for line in text_blocks[-1]:
    instr = list(map(int, line.split()))
    execute(opscode_map[instr[0]], instr[1], instr[2], instr[3], reg)
ans2 = reg[0]
print("part 2:", ans2)

from utils import load_lines
import re
from collections import defaultdict

INPUT_FILE = "./year2017/data/day25.txt"
MOVES = {"left": -1, "right": +1}


def load_turing_machine(filename):
    lines = load_lines(filename)
    state_start = re.compile(r"Begin in state ([A-Z]+).").match(lines[0]).group(1)
    steps = re.compile(r"Perform a diagnostic checksum after (\d+) steps.").match(lines[1]).group(1)
    turing = {}
    for i in range((len(lines) - 2) // 10):
        state = re.compile(r"In state ([A-Z]+):").match(lines[i * 10 + 3]).group(1)
        for j in range(2):
            value = re.compile(r".*If the current value is (\d+):").match(lines[i * 10 + j * 4 + 4]).group(1)
            write = re.compile(r".*Write the value (\d+).").match(lines[i * 10 + j * 4 + 5]).group(1)
            move = re.compile(r".*Move one slot to the ([a-z]+).").match(lines[i * 10 + j * 4 + 6]).group(1)
            state_next = re.compile(r".*Continue with state ([A-Z]+).").match(lines[i * 10 + j * 4 + 7]).group(1)
            turing[state, int(value)] = (int(write), MOVES[move], state_next)
    return turing, state_start, int(steps)


turing, state, steps = load_turing_machine(INPUT_FILE)
tape, cursor = defaultdict(int), 0
for _ in range(steps):
    value = tape[cursor]
    write, move, next = turing[state, value]
    tape[cursor] = write
    cursor += move
    state = next
print("part 1:", sum(tape.values()))

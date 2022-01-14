from utils import load_int_program
from IntcodeComputer import IntcodeComputer
from itertools import permutations

INPUT_FILE = "./year2019/data/day07.txt"


def run_amplifiers(program, seq, loop=False):
    amplifier = []
    for i in range(5):
        amplifier += [IntcodeComputer(program)]
        amplifier[i].input += [seq[i]]
    output = 0
    while True:
        for i in range(5):
            amplifier[i].input += [output]
            amplifier[i].run()
            output = amplifier[i].output[-1]
        if not loop or amplifier[4].finished:
            return output


program = load_int_program(INPUT_FILE)
ans1 = 0
for seq in permutations([0, 1, 2, 3, 4]):
    ans1 = max(ans1, run_amplifiers(program, seq))
print("part 1:", ans1)

ans2 = 0
for seq in permutations([5, 6, 7, 8, 9]):
    ans2 = max(ans2, run_amplifiers(program, seq, True))
print("part 2:", ans2)

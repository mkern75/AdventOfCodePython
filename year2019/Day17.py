from utils import load_int_program
from IntcodeComputer import IntcodeComputer

INPUT_FILE = "./year2019/data/day17.txt"

program = load_int_program(INPUT_FILE)
computer = IntcodeComputer(program)
computer.run()
scaffolds = [list(row) for row in computer.get_ascii_output().split("\n") if row != ""]
h, w = len(scaffolds), len(scaffolds[0])

# part 1
res1 = 0
for r in range(1, h - 1):
    for c in range(1, w - 1):
        if 0 < r < h - 1 and 0 < c < w - 1:
            if all(scaffolds[r + dr][c + dc] != "." for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]):
                res1 += r * c
print("part 1:", res1)

# print camera feed
# for r in range(h):
#     print("".join(scaffolds[r][c] for c in range(w)))

# part 2: manual solution
program[0] = 2
computer.reset(program)
computer.add_ascii_input("A,B,A,B,A,C,B,C,A,C\n")
computer.add_ascii_input("L,10,L,12,R,6\n")
computer.add_ascii_input("R,10,L,4,L,4,L,12\n")
computer.add_ascii_input("L,10,R,10,R,6,L,4\n")
computer.add_ascii_input("n\n")
computer.run()

res2 = computer.pop_last_output()
print("part 2:", res2)

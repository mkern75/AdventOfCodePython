INPUT_FILE = "./year2022/data/day10.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

X = [None, 1]
for instr in data:
    X += [X[-1]]
    if instr.startswith("addx"):
        X += [X[-1] + int(instr[5:])]
print(f"part 1: {sum(c * X[c] for c in range(20, len(X), 40))}")

print(f"part 2:")
for i in range(0, 240):
    print("#" if X[i + 1] - 1 <= i % 40 <= X[i + 1] + 1 else ".", end="")
    if i % 40 == 39:
        print()

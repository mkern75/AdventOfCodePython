from colorama import Back, Style

INPUT_FILE = "./year2022/data/day10.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

x = [None, 1]
for instr in data:
    if instr == "noop":
        x += [x[-1]]
    elif instr.startswith("addx"):
        x += [x[-1]]
        x += [x[-1] + int(instr[5:])]
    else:
        assert False
print(f"part 1: {sum(c * x[c] for c in range(20, len(x), 40))}")

print(f"part 2:")
for i in range(0, 240):
    print(Back.WHITE + "##" + Style.RESET_ALL if abs(i % 40 - x[i + 1]) <= 1 else "..", end="")
    if i % 40 == 39:
        print()

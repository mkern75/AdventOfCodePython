from utils import load_number, tic, toc

INPUT_FILE = "./year2017/data/day17.txt"

tic()
steps = load_number(INPUT_FILE)
buffer = [0]
pos = 0
for i in range(1, 2017 + 1):
    pos = (pos + steps) % len(buffer)
    buffer = buffer[:pos + 1] + [i] + buffer[pos + 1:]
    pos += 1
ans1 = buffer[(pos + 1) % len(buffer)]
print(f"part 1: {ans1}  ({toc():.3f}s)")

tic()
pos = 0  # current position
pos_0 = 0  # position of 0
after_0 = 0  # element after 0 (only changes if we insert directly after 0)
for i in range(1, 50000000 + 1):
    pos = (pos + steps) % i
    if pos < pos_0:
        pos_0 += 1
    elif pos == pos_0:
        after_0 = i
    pos += 1
ans2 = after_0
print(f"part 2: {ans2}  ({toc():.3f}s)")

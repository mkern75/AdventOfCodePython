from time import time

time_start = time()
INPUT_FILE = "./year2025/data/day01.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0
pos, mod = 50, 100
for line in data:
    direction, distance = line[0], int(line[1:])
    ans2 += distance // mod
    distance %= mod
    pos_prev, pos = pos, pos + (-distance if direction == "L" else +distance)
    if pos_prev != 0 and (pos <= 0 or pos >= mod):
        ans2 += 1
    pos %= mod
    if pos == 0:
        ans1 += 1

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")
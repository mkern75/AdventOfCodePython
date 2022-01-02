import time

t0 = time.time()
INPUT_FILE = "./year2020/data/day01.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
n = [int(line) for line in lines]

for i in range(len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == 2020:
            ans1 = n[i] * n[j]
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

for i in range(len(n) - 2):
    for j in range(i + 1, len(n) - 1):
        for k in range(j + 1, len(n)):
            if n[i] + n[j] + n[k] == 2020:
                ans2 = n[i] * n[j] * n[k]
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

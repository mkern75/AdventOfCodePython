import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day13.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

R = {}
for line in lines:
    d, r = list(map(int, line.replace(":", "").split()))
    R[d] = r
D = max(R.keys())

severity = 0
for d in range(0, D + 1):
    if d in R:
        if d % ((R[d] - 1) * 2) == 0:
            severity += d * R[d]
print("part 1:", severity, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

delay = 9
stop = False
while not stop:
    delay += 1
    stop = True
    for d in range(0, D + 1):
        if d in R:
            if (d + delay) % ((R[d] - 1) * 2) == 0:
                stop = False
print("part 2:", delay, f"  ({time.time() - t1:.3f}s)")

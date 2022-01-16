from utils import load_lines, tic, toc

INPUT_FILE = "./year2017/data/day13.txt"

tic()
R = {}
for line in load_lines(INPUT_FILE):
    d, r = list(map(int, line.replace(":", "").split()))
    R[d] = r
D = max(R.keys())

severity = 0
for d in range(0, D + 1):
    if d in R:
        if d % ((R[d] - 1) * 2) == 0:
            severity += d * R[d]
print(f"part 1: {severity}  ({toc():.3f}s)")

tic()
delay = 9
stop = False
while not stop:
    delay += 1
    stop = True
    for d in range(0, D + 1):
        if d in R:
            if (d + delay) % ((R[d] - 1) * 2) == 0:
                stop = False
print(f"part 2: {delay}  ({toc():.3f}s)")

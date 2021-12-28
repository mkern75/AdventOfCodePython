from datetime import datetime

INPUT_FILE = "./year2016/data/day19.txt"


def next(i, elf):
    i = (i + 1) % len(elf)
    while not elf[i]:
        i = (i + 1) % len(elf)
    return i


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

N = int(lines[0])

elf = [True] * N
i, cnt = 0, 0
while cnt < N - 1:
    i = next(i, elf)
    elf[i] = False
    cnt += 1
    i = next(i, elf)
ans1 = elf.index(True) + 1
print("part 1:", ans1)

elf = [True] * N
i, cnt = 0, 0
j, odd = N // 2, N % 2 == 1
while cnt < N - 1:
    elf[j] = False
    cnt += 1
    i = next(i, elf)
    j = next(j, elf)
    if odd:
        j = next(j, elf)
    odd = not odd
ans2 = elf.index(True) + 1
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

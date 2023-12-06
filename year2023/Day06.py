INPUT_FILE = "./year2023/data/day06.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

for part in [1, 2]:
    if part == 1:
        time = list(map(int, data[0].split(":")[1].split()))
        dist = list(map(int, data[1].split(":")[1].split()))
    else:
        time = [int(data[0].split(":")[1].replace(" ", ""))]
        dist = [int(data[1].split(":")[1].replace(" ", ""))]

    ans = 1

    for t, d in zip(time, dist):
        ans *= sum((t - i) * i > d for i in range(t + 1))

    print(f"part {part}: {ans}")

file = open("./year2021/data/day13.txt", "r")
lines = [line.rstrip('\n') for line in file]

ans1 = -1
P = set([])
for line in lines:
    if "," in line:
        x, y = map(int, line.split(","))
        P.add((x, y))
    elif "fold along" in line:
        before, fold = line.split("=")
        fold = int(fold)
        FP = set([])
        for (x, y) in P:
            if "x" in line:
                FP.add((x, y) if x < fold else (2 * fold - x, y))
            else:
                FP.add((x, y) if y < fold else (x, 2 * fold - y))
        P = FP
        if ans1 == -1:
            ans1 = len(P)
print(ans1)

R = max([y for (x, y) in P]) + 1
C = max([x for (x, y) in P]) + 1
for r in range(R):
    for c in range(C):
        print("#" if (c, r) in P else " ", end="")
    print("")

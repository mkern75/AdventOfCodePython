from datetime import datetime

file = open("./year2021/data/day25.txt", "r")
lines = [line.rstrip('\n') for line in file]


def one_step(g):
    R, C, move = len(lines), len(lines[0]), False
    ng = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if g[r][c] == 1:
                if g[r][(c + 1) % C] == 0:
                    ng[r][(c + 1) % C] = 1
                    move = True
                else:
                    ng[r][c] = 1
    for r in range(R):
        for c in range(C):
            if g[r][c] == 2:
                if g[(r + 1) % R][c] != 2 and ng[(r + 1) % R][c] == 0:
                    ng[(r + 1) % R][c] = 2
                    move = True
                else:
                    ng[r][c] = 2
    return move, ng


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

m = {".": 0, ">": 1, "v": 2}
G = [[m[c] for c in line] for line in lines]

step, move = 0, True
while move:
    step += 1
    move, G = one_step(G)
print("part 1:", step)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

file = open("./year2021/data/day25.txt", "r")
lines = [line.rstrip('\n') for line in file]
G = [[c for c in line] for line in lines]


def one_step(g):
    R, C, move = len(g), len(g[0]), False
    ng = [["."] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if g[r][c] == ">":
                if g[r][(c + 1) % C] == ".":
                    ng[r][(c + 1) % C] = ">"
                    move = True
                else:
                    ng[r][c] = ">"
    for r in range(R):
        for c in range(C):
            if g[r][c] == "v":
                if g[(r + 1) % R][c] != "v" and ng[(r + 1) % R][c] == ".":
                    ng[(r + 1) % R][c] = "v"
                    move = True
                else:
                    ng[r][c] = "v"
    return move, ng


step, move = 0, True
while move:
    step += 1
    move, G = one_step(G)
print("part 1:", step)

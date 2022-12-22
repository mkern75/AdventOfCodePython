INPUT_FILE = "./year2022/data/day22.txt"
segments = [[line.rstrip('\n') for line in x.splitlines()] for x in open(INPUT_FILE).read().split("\n\n")]

# load board (0-based index) and path
board = {(r, c): tile for r, line in enumerate(segments[0]) for c, tile in enumerate(line) if tile != " "}
path = segments[1][0].replace("R", " R ").replace("L", " L ").split()
path = [int(x) if x.isdigit() else x for x in path]


def turn(dr, dc, mv):
    return (-dc, dr) if mv == "L" else (dc, -dr)


def move(r, c, dr, dc):
    rn, cn = r + dr, c + dc
    if (r + dr, c + dc) not in board:
        if dc == 1:
            rn, cn = r, min(cc for rr, cc in board if rr == r)
        elif dc == -1:
            rn, cn = r, max(cc for rr, cc in board if rr == r)
        elif dr == 1:
            rn, cn = min(rr for rr, cc in board if cc == c), c
        elif dr == -1:
            rn, cn = max(rr for rr, cc in board if cc == c), c
    if board[rn, cn] == ".":
        return rn, cn
    else:
        return r, c


r, c = 0, min(cc for rr, cc in board if rr == 0 and board[rr, cc] == ".")
dr, dc = 0, 1
for mv in path:
    if mv in ["L", "R"]:
        dr, dc = turn(dr, dc, mv)
    else:
        for _ in range(mv):
            r, c = move(r, c, dr, dc)
ans1 = 1000 * (r + 1) + 4 * (c + 1) + {(0, 1): 0, (0, -1): 2, (1, 0): 1, (-1, 0): 3}[dr, dc]
print(f"part 1: {ans1}")

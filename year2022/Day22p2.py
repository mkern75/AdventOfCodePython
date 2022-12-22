from math import isqrt

INPUT_FILE = "./year2022/data/day22.txt"
segments = [[line.rstrip('\n') for line in x.splitlines()] for x in open(INPUT_FILE).read().split("\n\n")]

# board (0-based index) and path information
board = {(r, c): tile for r, line in enumerate(segments[0]) for c, tile in enumerate(line) if tile != " "}
N = isqrt(len(board) // 6)
path = segments[1][0].replace("R", " R ").replace("L", " L ").split()
path = [int(x) if x.isdigit() else x for x in path]


def turn(dr, dc, mv):
    return (-dc, dr) if mv == "L" else (dc, -dr)


# this method only works for the specific shape of the cube net in my puzzle input
# todo: generalise so that it works with any net shape
def move2(r, c, dr, dc):
    rn, cn = r + dr, c + dc
    drn, dcn = dr, dc
    if (rn, cn) not in board:
        if 0 <= rn < N and cn == N - 1 and dc == -1:
            rn, cn = 2 * N + (N - 1 - rn), 0
            drn, dcn = 0, 1
        elif rn == - 1 and N <= cn < 2 * N and dr == -1:
            rn, cn = 3 * N + cn - N, 0
            drn, dcn = 0, 1
        elif rn == - 1 and 2 * N <= cn < 3 * N and dr == -1:
            rn, cn = 4 * N - 1, cn - 2 * N
            drn, dcn = -1, 0
        elif rn == N and 2 * N <= cn < 3 * N and dr == 1:
            rn, cn = N + (cn - 2 * N), 2 * N - 1
            drn, dcn = 0, -1
        elif 0 <= rn < N and cn == 3 * N and dc == 1:
            rn, cn = 3 * N - 1 - rn, 2 * N - 1
            drn, dcn = 0, -1
        elif N <= rn < 2 * N and cn == N - 1 and dc == -1:
            rn, cn = 2 * N, rn - N
            drn, dcn = 1, 0
        elif N <= rn < 2 * N and cn == 2 * N and dc == 1:
            rn, cn = N - 1, 2 * N + (rn - N)
            drn, dcn = -1, 0
        elif 2 * N <= rn < 3 * N and cn == - 1 and dc == -1:
            rn, cn = 3 * N - 1 - rn, N
            drn, dcn = 0, 1
        elif rn == 2 * N - 1 and 0 <= cn < N and dr == -1:
            rn, cn = N + cn, N
            drn, dcn = 0, 1
        elif rn == 3 * N and N <= cn < 2 * N and dr == 1:
            rn, cn = 3 * N + (cn - N), N - 1
            drn, dcn = 0, -1
        elif 2 * N <= rn < 3 * N and cn == 2 * N and dc == 1:
            rn, cn = 3 * N - 1 - rn, 3 * N - 1
            drn, dcn = 0, -1
        elif 3 * N <= rn < 4 * N and cn == -1 and dc == -1:
            rn, cn = 0, N + (rn - 3 * N)
            drn, dcn = 1, 0
        elif rn == 4 * N and 0 <= cn < N and dr == 1:
            rn, cn = 0, 2 * N + cn
            drn, dcn = 1, 0
        elif 3 * N <= rn < 4 * N and cn == N and dc == 1:
            rn, cn = 3 * N - 1, N + (rn - 3 * N)
            drn, dcn = -1, 0
        else:
            assert False
    if board[rn, cn] == ".":
        return rn, cn, drn, dcn
    else:
        return r, c, dr, dc


r, c = 0, min(cc for rr, cc in board if rr == 0 and board[rr, cc] == ".")
dr, dc = 0, 1
for mv in path:
    if mv in ["L", "R"]:
        dr, dc = turn(dr, dc, mv)
    else:
        for _ in range(mv):
            r, c, dr, dc = move2(r, c, dr, dc)
ans2 = 1000 * (r + 1) + 4 * (c + 1) + {(0, 1): 0, (0, -1): 2, (1, 0): 1, (-1, 0): 3}[dr, dc]
print(f"part 2: {ans2}")

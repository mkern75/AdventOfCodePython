import numpy as np

file = open("./year2015/data/day18.txt", "r")
lines = [line.rstrip('\n') for line in file]


def one_step_game_of_life(L, keep_corners_on=False):
    dim = len(L)
    NL = np.zeros((dim, dim), dtype=int)
    for r in range(dim):
        for c in range(dim):
            cnt = 0
            for (rn, cn) in [(r + 1, c), (r + 1, c + 1), (r, c + 1), (r - 1, c + 1), (r - 1, c), (r - 1, c - 1),
                             (r, c - 1), (r + 1, c - 1)]:
                if 0 <= rn < dim and 0 <= cn < dim and L[rn][cn] == 1:
                    cnt += 1
            if (L[r][c] == 1 and cnt in [2, 3]) or (L[r][c] == 0 and cnt == 3):
                NL[r][c] = 1
            elif keep_corners_on and (r, c) in [(0, 0), (0, dim - 1), (dim - 1, 0), (dim - 1, dim - 1)]:
                NL[r][c] = 1
    return NL


START = [[int(c == "#") for c in line] for line in lines]
L = np.array(START)
for step in range(100):
    L = one_step_game_of_life(L)
print(np.sum(L))

L = np.array([[int(c == "#") for c in line] for line in lines])
dim = len(L)
L[0][0] = L[dim - 1][0] = L[0][dim - 1] = L[dim - 1][dim - 1] = 1
for step in range(100):
    L = one_step_game_of_life(L, True)
print(np.sum(L))

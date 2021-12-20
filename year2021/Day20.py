import numpy as np

file = open("./year2021/data/day20.txt", "r")
lines = [line.rstrip('\n') for line in file]


def index(img, r, c, dv):
    idx = 0
    b = 256
    for rr in range(r - 1, r + 2):
        for cc in range(c - 1, c + 2):
            if 0 <= rr < len(img) and 0 <= cc < len(img):
                idx += b * img[rr][cc]
            else:
                idx += b * dv
            b //= 2
    return idx


def enhance(img, dv):
    new_n = len(img) + 2
    new_img = np.zeros((new_n, new_n), dtype=int)
    for r in range(new_n):
        for c in range(new_n):
            new_img[r][c] = alg[index(img, r - 1, c - 1, dv)]
    new_dv = alg[index(img, -10, -10, dv)]
    return new_img, new_dv


alg = [int(c == "#") for c in lines[0]]

N = len(lines) - 2
img = np.zeros((N, N), dtype=int)
for r in range(N):
    for c in range(N):
        img[r][c] = 1 if lines[r + 2][c] == "#" else 0
dv = 0  # default value everywhere else

for t in range(1, 50 + 1):
    img, dv = enhance(img, dv)
    if t in [2, 50]:
        print(t, np.sum(img))

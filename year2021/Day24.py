import functools
from datetime import datetime

file = open("./year2021/data/day24.txt", "r")
lines = [line.rstrip('\n') for line in file]
prog = [line.split() for line in lines]

A, B, C = [], [], []
for i in range(14):
    A += [int(prog[i * 18 + 4][2])]
    B += [int(prog[i * 18 + 5][2])]
    C += [int(prog[i * 18 + 15][2])]


@functools.lru_cache(maxsize=None)
def run_program(depth, z, maximise=True):
    if depth == 14:
        return "" if z == 0 else None

    fr, to, step = 9, 0, -1
    if not maximise:
        fr, to, step = 1, 10, 1
    for d in range(fr, to, step):
        if z % 26 == d - B[depth]:
            z_new = z // A[depth]
        else:
            z_new = (z // A[depth]) * 26 + d + C[depth]
        result = run_program(depth + 1, z_new, maximise)
        if result is not None:
            return str(d) + result
    return None


print("start :", datetime.now().strftime("%H:%M:%S.%f"))
print("part 1:", run_program(0, 0, True))
print("part 2:", run_program(0, 0, False))
print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

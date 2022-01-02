import time
import functools

t0 = time.time()
INPUT_FILE = "./year2017/data/day16.txt"

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
MOVES = lines[0].split(",")


@functools.lru_cache(maxsize=None)  # DP with a single line of code!
def dance(programs):
    p = [c for c in programs]
    for move in MOVES:
        if move[0] == "s":
            x = int(move[1:])
            p = p[-x:] + p[:-x]
        elif move[0] == "x":
            a, b = map(int, move[1:].split("/"))
            tmp = p[a]
            p[a] = p[b]
            p[b] = tmp
        elif move[0] == "p":
            a, b = move[1:].split("/")
            ia, ib = p.index(a), p.index(b)
            tmp = p[ia]
            p[ia] = p[ib]
            p[ib] = tmp
    return "".join(p)


programs = "abcdefghijklmnop"
ans1 = dance(programs)
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

programs = "abcdefghijklmnop"
i = 0
dance_hist = {programs: i}
while True:
    i += 1
    programs = dance(programs)
    if i == 1000000000:  # end reached?
        ans2 = programs
        break
    if programs in dance_hist:  # seen before? => cycle
        di = i - dance_hist[programs]
        m = 1000000000 % di
        for key, val in dance_hist.items():
            if val == dance_hist[programs] + m:
                ans2 = key
                break
        break
    else:
        dance_hist[programs] = i
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

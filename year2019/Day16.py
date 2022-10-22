from utils import load_word, tic, toc

INPUT_FILE = "./year2019/data/day16.txt"
PATTERN = [0, 1, 0, -1]


def one_phase(l):
    n = len(l)
    ll = [0] * n
    print(len(l))
    for i in range(n):
        x = 0
        if i % 10000 == 0:
            print(i, len(l))
        for j in range(i, n):
            idx = ((j + 1) % ((i + 1) * 4)) // (i + 1)
            if idx == 1:
                x += l[j]
            elif idx == 3:
                x -= l[j]
        ll[i] = abs(x) % 10
    return ll

# tic()
w = load_word(INPUT_FILE)
#
# l = [int(i) for i in w]
#
# for p in range(1, 101):
#     l = one_phase(l)
# ans1 = "".join([str(i) for i in l[0:8]])
# print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
l = []
for _ in range(10000):
    l.extend([int(i) for i in w])
for p in range(1, 101):
    l = one_phase(l)
    print(f"phase: {p}   ({toc():.3f}s)")

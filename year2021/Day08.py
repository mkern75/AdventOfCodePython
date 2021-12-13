import itertools as it

file = open("./year2021/data/day08.txt", "r")
lines = [line.rstrip('\n') for line in file]

SEGMENTS = "abcdefg"
DIGITS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

p1 = 0
for line in lines:
    y = line.split(" | ")[1].split()
    for n in y:
        if len(n) in [2, 3, 4, 7]:
            p1 += 1
print(p1)


def map_orig(ll, d):
    r = []
    for s in ll:
        v = ""
        for c in s:
            v += d[c]
        r.append(''.join(sorted(v)))
    return r


p2 = 0
for line in lines:
    t = line.split(" | ")
    x, y = t[0].split(), t[1].split()
    for perm in it.permutations(SEGMENTS):
        m = {i: j for i, j in zip(perm, SEGMENTS)}
        if set(DIGITS) == set(map_orig(x, m)):
            r = map_orig(y, m)
            d = [DIGITS.index(i) for i in r]
            p2 += 1000 * d[0] + 100 * d[1] + 10 * d[2] + d[3]
            break
print(p2)

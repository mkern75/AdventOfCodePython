from itertools import permutations
from collections import defaultdict

file = open("./year2015/data/day13.txt", "r")
lines = [line.rstrip('\n') for line in file]

P = set()  # people
H = defaultdict(int)  # happiness
for line in lines:
    s = line.split()
    p1, p2 = s[0], s[10].replace(".", "")
    P.update({p1, p2})
    H[(p1, p2)] = int(s[3]) * (+1 if s[2] == "gain" else -1)

N = len(P)
best = 0
for perm in permutations(P):
    h = 0
    for i in range(N):
        h += H[(perm[i], perm[(i - 1) % N])] + H[(perm[i], perm[(i + 1) % N])]
    best = max(best, h)
print(best)

P.update({"I"})
N = len(P)
best = 0
for perm in permutations(P):
    h = 0
    for i in range(N):
        h += H[(perm[i], perm[(i - 1) % N])] + H[(perm[i], perm[(i + 1) % N])]
    best = max(best, h)
print(best)

from utils import load_words
from collections import Counter
from itertools import combinations

INPUT_FILE = "./year2018/data/day02.txt"


def overlapping(s1, s2):
    s = ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            s += s1[i]
    return s


words = load_words(INPUT_FILE)

twos, threes = 0, 0
for w in words:
    twos += 1 if 2 in Counter(w).values() else 0
    threes += 1 if 3 in Counter(w).values() else 0
checksum = twos * threes
print("part 1:", checksum)

for w1, w2 in combinations(words, 2):
    w = overlapping(w1, w2)
    if len(w) == len(w1) - 1:
        print("part 2:", w)
        break

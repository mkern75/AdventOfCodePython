from utils import load_line

INPUT_FILE = "./year2017/data/day10.txt"


def reverse(l, rev_length, pos, skip):
    l2 = l.copy()
    for i in range(rev_length):
        l2[(pos + i) % len(l)] = l[(pos + rev_length - 1 - i) % len(l)]
    pos = (pos + rev_length + skip) % len(l)
    skip += 1
    return l2, pos, skip


line = load_line(INPUT_FILE)

seq_rev_lengths = [int(i) for i in line.split(",")]
L = [i for i in range(256)]
pos, skip = 0, 0
for rev_length in seq_rev_lengths:
    L, pos, skip = reverse(L, rev_length, pos, skip)

ans1 = L[0] * L[1]
print("part 1:", ans1)

seq_rev_lengths = [ord(c) for c in line] + [17, 31, 73, 47, 23]
L = [i for i in range(256)]
pos, skip = 0, 0
for _ in range(64):
    for rev_length in seq_rev_lengths:
        L, pos, skip = reverse(L, rev_length, pos, skip)
knot_hash = ""
for i in range(16):
    xor = 0
    for j in range(16):
        xor = xor ^ L[i * 16 + j]
    knot_hash += hex(xor)[2:].zfill(2)

ans2 = knot_hash
print("part 2:", ans2)

from time import time
from functools import cache

time_start = time()
INPUT_FILE = "./year2024/data/day21.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]

keypad_numeric = ["789", "456", "123", "X0A"]
keypad_directional = ["X^A", "<v>"]


def find_position(key, keypad):
    for r, row in enumerate(keypad):
        for c, char in enumerate(row):
            if char == key:
                return r, c
    assert False


def build_shortest_paths_between_keys(key1, key2, keypad):
    r1, c1 = find_position(key1, keypad)
    r2, c2 = find_position(key2, keypad)
    rx, cx = find_position("X", keypad)
    dr, dc = r2 - r1, c2 - c1

    row_moves = "v" * abs(dr) if dr >= 0 else "^" * abs(dr)
    col_moves = ">" * abs(dc) if dc >= 0 else "<" * abs(dc)

    if dr == dc == 0:
        return [""]
    elif dr == 0:
        return [col_moves]
    elif dc == 0:
        return [row_moves]
    elif (rx, cx) == (r1, c2):
        return [row_moves + col_moves]
    elif (rx, cx) == (r2, c1):
        return [col_moves + row_moves]
    else:
        return [row_moves + col_moves, col_moves + row_moves]


def build_sequence_of_shortest_paths(seq, keypad):
    res = []
    for key1, key2 in zip("A" + seq, seq):
        res += [[sp + "A" for sp in build_shortest_paths_between_keys(key1, key2, keypad)]]
    return res


@cache
def solve(seq, depth):
    if depth == 1:
        return len(seq)

    if any(c in seq for c in "012345679"):
        keypad = keypad_numeric
    else:
        keypad = keypad_directional

    res = 0
    for shortest_paths in build_sequence_of_shortest_paths(seq, keypad):
        res += min(solve(sp, depth - 1) for sp in shortest_paths)
    return res


ans1 = 0
for line in data:
    ans1 += solve(line, 1 + 2 + 1) * int(line[:3])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for line in data:
    ans2 += solve(line, 1 + 25 + 1) * int(line[:3])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

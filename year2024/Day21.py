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

    row_move = "v" * abs(dr) if dr >= 0 else "^" * abs(dr)
    col_move = ">" * abs(dc) if dc >= 0 else "<" * abs(dc)

    if dr == dc == 0:
        return [""]
    elif dr == 0:
        return [col_move]
    elif dc == 0:
        return [row_move]
    elif (rx, cx) == (r1, c2):
        return [row_move + col_move]
    elif (rx, cx) == (r2, c1):
        return [col_move + row_move]
    else:
        return [row_move + col_move, col_move + row_move]


def build_sequence_of_shortest_paths(seq, keypad):
    res = []
    for key1, key2 in zip("A" + seq, seq):
        res += [[sp + "A" for sp in build_shortest_paths_between_keys(key1, key2, keypad)]]
    return res


@cache
def calc(seq, depth):
    if depth == 0:
        return len(seq)
    return solve(build_sequence_of_shortest_paths(seq, keypad_directional), depth - 1)


def solve(seq_shortest_paths, depth):
    res = 0
    for shortest_paths in seq_shortest_paths:
        res += min(calc(sp, depth) for sp in shortest_paths)
    return res


ans1 = 0
for line in data:
    seq_sp_initial = build_sequence_of_shortest_paths(line, keypad_numeric)
    ans1 += solve(seq_sp_initial, 2) * int(line[:3])
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

ans2 = 0
for line in data:
    seq_sp_initial = build_sequence_of_shortest_paths(line, keypad_numeric)
    ans2 += solve(seq_sp_initial, 25) * int(line[:3])
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

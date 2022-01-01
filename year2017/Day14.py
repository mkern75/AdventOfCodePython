import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day14.txt"


def reverse(l, rev_length, pos, skip):
    l2 = l.copy()
    for i in range(rev_length):
        l2[(pos + i) % len(l)] = l[(pos + rev_length - 1 - i) % len(l)]
    pos = (pos + rev_length + skip) % len(l)
    skip += 1
    return l2, pos, skip


def knot_hash(key):
    seq_rev_lengths = [ord(c) for c in key] + [17, 31, 73, 47, 23]
    L = [i for i in range(256)]
    pos, skip = 0, 0
    for _ in range(64):
        for rev_length in seq_rev_lengths:
            L, pos, skip = reverse(L, rev_length, pos, skip)
    result = ""
    for i in range(16):
        xor = 0
        for j in range(16):
            xor = xor ^ L[i * 16 + j]
        result += hex(xor)[2:].zfill(2)
    result = result.zfill(32)
    return result


def build_grid(key):
    grid = []
    for r in range(128):
        h = knot_hash(key + "-" + str(r))
        b = (bin(int(h, 16))[2:]).zfill(len(h) * 4)
        grid += [["#" if c == "1" else "." for c in b]]
    return grid


def remove_region(row, col, grid_bool):
    grid_bool[row][col] = False
    for rn, cn in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if 0 <= rn < 128 and 0 <= cn < 128:
            if grid_bool[rn][cn]:
                remove_region(rn, cn, grid_bool)


def count_regions(grid):
    cnt = 0
    grid_bool = [[True if grid[r][c] == "#" else False for c in range(128)] for r in range(128)]
    for row in range(128):
        for col in range(128):
            if grid_bool[row][col]:
                cnt += 1
                remove_region(row, col, grid_bool)
    return cnt


file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

grid = build_grid(lines[0])
ans1 = sum(row.count("#") for row in grid)
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = count_regions(grid)
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

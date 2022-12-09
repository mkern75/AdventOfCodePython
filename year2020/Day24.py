INPUT_FILE = "./year2020/data/day24.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

MOVES = {"e": (1, 0), "w": (-1, 0), "nw": (0, 1), "ne": (1, 1), "se": (0, -1), "sw": (-1, -1)}


def coord(tile):
    if tile == "":
        return 0, 0
    m = next(m for m in MOVES if tile.startswith(m))
    c = coord(tile[len(m):])
    return MOVES[m][0] + c[0], MOVES[m][1] + c[1]


def flip(black):
    black_new = set()
    to_check = set(black) | set([(c[0] + dx, c[1] + dy) for dx, dy in MOVES.values() for c in black])
    for c in to_check:
        n = sum((c[0] + dx, c[1] + dy) in black for dx, dy in MOVES.values())
        if (c in black and n in [1, 2]) or (c not in black and n == 2):
            black_new.add(c)
    return black_new


black = set()
for move in data:
    c = coord(move)
    if c in black:
        black.remove(c)
    else:
        black.add(c)
print(f"part 1: {len(black)}")

for day in range(100):
    black = flip(black)
print(f"part 2: {len(black)}")

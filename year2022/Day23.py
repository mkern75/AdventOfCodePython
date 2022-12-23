from collections import Counter
from math import inf

NEIGBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0,), (1, -1), (0, -1)]
DIRECTIONS = [[(-1, 0), (-1, -1), (-1, 1)],
              [(1, 0), (1, -1), (1, 1)],
              [(0, -1), (1, -1), (-1, -1)],
              [(0, 1), (1, 1), (-1, 1)]]

INPUT_FILE = "./year2022/data/day23.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]


def move_elf(elf, elves, cycle):
    if not set((elf[0] + dr, elf[1] + dc) for dr, dc in NEIGBOURS) & elves:
        return elf
    for i in range(4):
        direction = DIRECTIONS[(cycle + i) % 4]
        if not set((elf[0] + dr, elf[1] + dc) for dr, dc in direction) & elves:
            return elf[0] + direction[0][0], elf[1] + direction[0][1]
    return elf


def moves_elves_single_cycle(elves, cycle):
    move, counter = {}, Counter()
    for elf in elves:
        move[elf] = move_elf(elf, elves, cycle)
        counter[move[elf]] += 1
    elves_new = set(move[elf] if counter[move[elf]] == 1 else elf for elf in elves)
    return elves_new, elves_new != elves


def moves_elves(elves, max_cycle=inf):
    cycle = 0  # zero-based
    while True:
        elves, have_moved = moves_elves_single_cycle(elves, cycle)
        cycle += 1
        if not have_moved or cycle == max_cycle:
            return elves, cycle


def count_tiles(elves):
    r_min, r_max = min(r for r, c in elves), max(r for r, c in elves)
    c_min, c_max = min(c for r, c in elves), max(c for r, c in elves)
    return sum((r, c) not in elves for r in range(r_min, r_max + 1) for c in range(c_min, c_max + 1))


# part 1
elves = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "#")
elves, _ = moves_elves(elves, 10)
print(f"part 1: {count_tiles(elves)}")

# part 2
elves = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "#")
elves, cycles = moves_elves(elves)
print(f"part 2: {cycles}")

from collections import Counter
from math import inf

NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0,), (1, -1), (0, -1)]
MOVES = [[(-1, 0), (-1, -1), (-1, 1)],  # N
         [(1, 0), (1, -1), (1, 1)],  # S
         [(0, -1), (1, -1), (-1, -1)],  # W
         [(0, 1), (1, 1), (-1, 1)]]  # E

INPUT_FILE = "./year2022/data/day23.txt"
grid = [[c for c in line.rstrip('\n')] for line in open(INPUT_FILE, "r")]


def move_elf(elf, elves, cycle):
    if not set((elf[0] + dr, elf[1] + dc) for dr, dc in NEIGHBOURS) & elves:
        return elf
    for i in range(4):
        move = MOVES[(cycle + i) % 4]
        if not set((elf[0] + dr, elf[1] + dc) for dr, dc in move) & elves:
            return elf[0] + move[0][0], elf[1] + move[0][1]
    return elf


def move_elves_single_cycle(elves, cycle):
    potential_move, counter = {}, Counter()
    for elf in elves:
        potential_move[elf] = move_elf(elf, elves, cycle)
        counter[potential_move[elf]] += 1
    elves_new = set(potential_move[elf] if counter[potential_move[elf]] == 1 else elf for elf in elves)
    return elves_new, elves_new != elves


def move_elves(elves, max_cycle=inf):
    cycle = 0  # zero-based
    while True:
        elves, have_moved = move_elves_single_cycle(elves, cycle)
        cycle += 1
        if cycle == max_cycle or not have_moved:
            return elves, cycle


def count_tiles(elves):
    r_min, r_max = min(r for r, c in elves), max(r for r, c in elves)
    c_min, c_max = min(c for r, c in elves), max(c for r, c in elves)
    return (r_max - r_min + 1) * (c_max - c_min + 1) - len(elves)


# part 1
elves = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "#")
elves, _ = move_elves(elves, 10)
print(f"part 1: {count_tiles(elves)}")

# part 2
elves = set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "#")
elves, cycles = move_elves(elves)
print(f"part 2: {cycles}")

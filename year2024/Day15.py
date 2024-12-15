from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day15.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


class Warehouse:
    MOVES = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    SCALING = {".": "..", "#": "##", "@": "@.", "O": "[]"}

    def __init__(self, data):
        self._grid = [list(line.rstrip("\n")) for line in data]  # type: list[list[str]]
        self._n_rows = len(self._grid)
        self._n_cols = len(self._grid[0])
        self._r_robot, self._c_robot = next(
            (r, c) for r in range(self._n_rows) for c in range(self._n_cols) if self._grid[r][c] == "@")

    def display(self, info=None):
        if info:
            print(info)
        for r in range(self._n_rows):
            print("".join(self._grid[r]))
        print()

    def sum_gps(self):
        return sum(100 * r + c for r in range(self._n_rows) for c in range(self._n_cols) if self._grid[r][c] in "O[")

    def scale_up(self):
        self._grid = [list("".join(Warehouse.SCALING[x] for x in row)) for row in self._grid]
        self._n_cols *= 2
        self._c_robot *= 2

    def execute_moves(self, moves, show_progress=False):
        if show_progress:
            self.display("Initial state:")
        for move in moves:
            self._move(move)
            if show_progress:
                self.display(f"Move {move}:")

    def _move(self, move):
        dr, dc = Warehouse.MOVES[move]

        to_move = [(self._r_robot, self._c_robot)]
        for r, c in to_move:
            if (r + dr, c + dc) not in to_move:
                if self._grid[r + dr][c + dc] == "#":
                    return
                if self._grid[r + dr][c + dc] in "O[]":
                    to_move.append((r + dr, c + dc))
                    if self._grid[r + dr][c + dc] == "[":
                        to_move.append((r + dr, c + dc + 1))
                    if self._grid[r + dr][c + dc] == "]":
                        to_move.append((r + dr, c + dc - 1))

        for r, c in reversed(to_move):
            self._grid[r + dr][c + dc] = self._grid[r][c]
            self._grid[r][c] = "."
        self._r_robot += dr
        self._c_robot += dc


moves = "".join(blocks[1])
warehouse = Warehouse(blocks[0])
warehouse.execute_moves(moves)
ans1 = warehouse.sum_gps()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

moves = "".join(blocks[1])
warehouse = Warehouse(blocks[0])
warehouse.scale_up()
warehouse.execute_moves(moves)
ans2 = warehouse.sum_gps()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

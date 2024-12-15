from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day15.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


class Warehouse:
    def __init__(self, data):
        self._grid = [list(line.rstrip("\n")) for line in data]  # type: list[list[str]]
        self._n_rows = len(self._grid)
        self._n_cols = len(self._grid[0])
        self._r_robot = -1
        self._c_robot = -1
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] == "@":
                    self._r_robot, self._c_robot = r, c

    def display(self, info=None):
        if info:
            print(info)
        for r in range(self._n_rows):
            print("".join(self._grid[r]))
        print()

    def gps(self):
        res = 0
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] in "O[":
                    res += 100 * r + c
        return res

    def scale_up(self):
        g = [["."] * (2 * self._n_cols) for _ in range(self._n_rows)]
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] in "#.":
                    g[r][2 * c] = self._grid[r][c]
                    g[r][2 * c + 1] = self._grid[r][c]
                elif self._grid[r][c] == "O":
                    g[r][2 * c] = "["
                    g[r][2 * c + 1] = "]"
                elif self._grid[r][c] == "@":
                    g[r][2 * c] = "@"
                    g[r][2 * c + 1] = "."
        self._grid = g
        self._n_cols *= 2
        self._c_robot *= 2

    def execute_moves(self, moves, show_progress=False):
        if show_progress:
            self.display("start:")
        for i, move in enumerate(moves, start=1):
            self._execute_move(move)
            if show_progress:
                self.display(f"move {i}: {move}")

    def _execute_move(self, move):
        if move == "<":
            self._move_horizontally(-1)
        elif move == ">":
            self._move_horizontally(+1)
        elif move == "^":
            self._move_vertically(-1)
        elif move == "v":
            self._move_vertically(+1)

    def _move_horizontally(self, dc):
        if self._grid[self._r_robot][self._c_robot + dc] == "#":
            return

        if self._grid[self._r_robot][self._c_robot + dc] == ".":
            self._grid[self._r_robot][self._c_robot] = "."
            self._c_robot += dc
            self._grid[self._r_robot][self._c_robot] = "@"
            return

        cc = self._c_robot + dc
        while self._grid[self._r_robot][cc] in "O[]":
            cc += dc

        if self._grid[self._r_robot][cc] != ".":
            return

        for c in range(cc, self._c_robot - dc, -dc):
            self._grid[self._r_robot][c] = self._grid[self._r_robot][c - dc]
        self._grid[self._r_robot][self._c_robot] = "."
        self._c_robot += dc

    def _move_vertically(self, dr):
        if self._grid[self._r_robot + dr][self._c_robot] == "#":
            return

        if self._grid[self._r_robot + dr][self._c_robot] == ".":
            self._grid[self._r_robot][self._c_robot] = "."
            self._r_robot += dr
            self._grid[self._r_robot][self._c_robot] = "@"
            return

        to_move = {(self._r_robot, self._c_robot)}
        while True:
            more_to_move = set()
            for r, c in to_move:
                if self._grid[r + dr][c] in "O[]" and (r + dr, c) not in to_move:
                    if self._grid[r + dr][c] == "O":
                        more_to_move.add((r + dr, c))
                    elif self._grid[r + dr][c] == "[":
                        more_to_move.add((r + dr, c))
                        more_to_move.add((r + dr, c + 1))
                    elif self._grid[r + dr][c] == "]":
                        more_to_move.add((r + dr, c - 1))
                        more_to_move.add((r + dr, c))
            to_move.update(more_to_move)
            if not more_to_move:
                break

        for r, c in to_move:
            if (r + dr, c) not in to_move and self._grid[r + dr][c] != ".":
                return

        for r, c in sorted(to_move, reverse=(dr == 1)):
            self._grid[r + dr][c] = self._grid[r][c]
            self._grid[r][c] = "."
        self._r_robot += dr


moves = "".join(blocks[1])
warehouse = Warehouse(blocks[0])
warehouse.execute_moves(moves)
ans1 = warehouse.gps()
print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")

moves = "".join(blocks[1])
warehouse = Warehouse(blocks[0])
warehouse.scale_up()
warehouse.execute_moves(moves)
ans2 = warehouse.gps()
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

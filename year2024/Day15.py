from time import time

time_start = time()

INPUT_FILE = "./year2024/data/day15.txt"
blocks = [block.splitlines() for block in open(INPUT_FILE, "r").read().split("\n\n")]


class Warehouse:
    MOVES = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    WALL, FREE, ROBOT, BOX, BOX_LEFT, BOX_RIGHT = "#", ".", "@", "O", "[", "]"

    def __init__(self, data):
        self._grid = [list(line.rstrip("\n")) for line in data]  # type: list[list[str]]
        self._n_rows = len(self._grid)
        self._n_cols = len(self._grid[0])
        self._r_robot = -1
        self._c_robot = -1
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] == Warehouse.ROBOT:
                    self._r_robot, self._c_robot = r, c

    def display(self, info=None):
        if info:
            print(info)
        for r in range(self._n_rows):
            print("".join(self._grid[r]))
        print()

    def sum_gps(self):
        res = 0
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] in [Warehouse.BOX, Warehouse.BOX_LEFT]:
                    res += 100 * r + c
        return res

    def scale_up(self):
        g = [[Warehouse.FREE] * (2 * self._n_cols) for _ in range(self._n_rows)]
        for r in range(self._n_rows):
            for c in range(self._n_cols):
                if self._grid[r][c] in [Warehouse.WALL, Warehouse.FREE]:
                    g[r][2 * c] = self._grid[r][c]
                    g[r][2 * c + 1] = self._grid[r][c]
                elif self._grid[r][c] == Warehouse.BOX:
                    g[r][2 * c] = Warehouse.BOX_LEFT
                    g[r][2 * c + 1] = Warehouse.BOX_RIGHT
                elif self._grid[r][c] == Warehouse.ROBOT:
                    g[r][2 * c] = Warehouse.ROBOT
                    g[r][2 * c + 1] = Warehouse.FREE
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
        dr, dc = Warehouse.MOVES[move]

        to_move = [(self._r_robot, self._c_robot)]
        for r, c in to_move:
            if (r + dr, c + dc) not in to_move:
                if self._grid[r + dr][c + dc] == Warehouse.WALL:
                    return
                if self._grid[r + dr][c + dc] in [Warehouse.BOX, Warehouse.BOX_LEFT, Warehouse.BOX_RIGHT]:
                    to_move.append((r + dr, c + dc))
                    if self._grid[r + dr][c + dc] == Warehouse.BOX_LEFT:
                        to_move.append((r + dr, c + dc + 1))
                    if self._grid[r + dr][c + dc] == Warehouse.BOX_RIGHT:
                        to_move.append((r + dr, c + dc - 1))

        for r, c in reversed(to_move):
            self._grid[r + dr][c + dc] = self._grid[r][c]
            self._grid[r][c] = Warehouse.FREE
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

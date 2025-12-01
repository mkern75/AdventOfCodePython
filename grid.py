class Grid:
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, data):
        self.grid = []
        for row in data:
            if type(row) is list:
                self.grid.append(row)
            else:
                self.grid.append(list(row))
        self.R = self.n_rows = len(self.grid)
        self.C = self.n_cols = len(self.grid[0])

    def get(self, r, c):
        return self.grid[r][c]

    def set(self, r, c, value):
        self.grid[r][c] = value

    def check(self, r, c, value):
        return self.grid[r][c] == value

    def find(self, v):
        g = self.grid
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if g[r][c] == v:
                    return r, c
        return None, None

    def valid(self, r, c):
        return r >= 0 and r < self.n_rows and c >= 0 and c < self.n_cols

    def inside(self, r, c):
        return self.valid(r, c)

    def outside(self, r, c):
        return not self.valid(r, c)

    def __repr__(self):
        s = []
        for row in self.grid:
            s.append("".join(row))
        return "\n".join(s)

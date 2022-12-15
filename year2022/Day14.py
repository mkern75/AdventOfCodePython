from collections import defaultdict

INPUT_FILE = "./year2022/data/day14.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]


def load_ground(data):
    ground = defaultdict(lambda: ".")
    for path in data:
        points = [tuple(map(int, point.split(","))) for point in path.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    ground[x, y] = "#"
    return ground


def count_sand(ground):
    res = 0
    y_freefall = max(coord[1] for coord in ground if ground[coord] == "#") + 1
    while True:
        x, y = 500, 0
        while True:
            if ground[x, y + 1] == ".":
                x, y = x, y + 1
            elif ground[x - 1, y + 1] == ".":
                x, y = x - 1, y + 1
            elif ground[x + 1, y + 1] == ".":
                x, y = x + 1, y + 1
            else:
                ground[x, y] = "o"
                res += 1
                if (x, y) == (500, 0):
                    return res
                break
            if y >= y_freefall:
                return res


ground = load_ground(data)
print(f"part 1: {count_sand(ground)}")

ground = load_ground(data)
rock_y_max = max(coord[1] for coord in ground if ground[coord] == "#")
for x in range(500 - (rock_y_max + 10), 500 + (rock_y_max + 10) + 1):  # sufficient width
    ground[x, rock_y_max + 2] = "#"
print(f"part 2: {count_sand(ground)}")
import re
from math import isqrt

INPUT_FILE = "./year2020/data/day20.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

SEA_MONSTER = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

# parse the input data
tiles, tile = {}, 0
for line in data:
    if reg := re.match(r"Tile (\d+):", line):
        tile = int(reg.groups()[0])
        tiles[tile] = []
    elif line != "":
        tiles[tile] += [list(line)]
N = isqrt(len(tiles))


def top(image):
    return image[0]


def bottom(image):
    return image[len(image) - 1]


def left(image):
    return [image[r][0] for r in range(len(image))]


def right(image):
    return [image[r][len(image[0]) - 1] for r in range(len(image))]


def version(image, v):
    """Return one of eight rotated + mirrored versions of the image."""
    for _ in range(v % 4):
        n_rows, n_cols = len(image), len(image[0])
        image = [[image[n_rows - r - 1][c] for r in range(n_rows)] for c in range(n_cols)]  # rotate
    for _ in range(v // 4):
        image = [r[::-1] for r in image]  # mirror
    return image


# establish potential neighbour tiles for each tile
tile_neighbours = {}
for tile, image in tiles.items():
    tile_neighbours[tile] = []
    for edge in [top(image), bottom(image), left(image), right(image)]:
        for tile2, image2 in tiles.items():
            if tile != tile2:
                edges2 = [top(image2), bottom(image2), left(image2), right(image2)]
                if edge in edges2 or edge[::-1] in edges2:
                    tile_neighbours[tile] += [tile2]


def arrange_tiles(tiles_remain, tiles_so_far, images_so_far):
    """Arrange tiles/images so that the borders all align."""
    if not tiles_remain:
        tiles_res = [[tiles_so_far[r * N + c] for c in range(N)] for r in range(N)]
        images_res = [[images_so_far[r * N + c] for c in range(N)] for r in range(N)]
        return tiles_res, images_res

    r, c = len(tiles_so_far) // N, len(tiles_so_far) % N
    idx_above = (r - 1) * N + c if r > 0 else None
    idx_left = r * N + c - 1 if c > 0 else None

    candidates = set(tiles_remain)  # candidates for next tile constrained by tiles already arranged
    if idx_above is not None:
        candidates &= set(tile_neighbours[tiles_so_far[idx_above]])
    if idx_left is not None:
        candidates &= set(tile_neighbours[tiles_so_far[idx_left]])

    for tile in candidates:
        for v in range(8):
            image = version(tiles[tile], v)
            if idx_above is None or bottom(images_so_far[idx_above]) == top(image):
                if idx_left is None or right(images_so_far[idx_left]) == left(image):
                    i = tiles_remain.index(tile)
                    if res := arrange_tiles(tiles_remain[:i] + tiles_remain[i + 1:], tiles_so_far + [tile],
                                            images_so_far + [image]):
                        return res
    return None


tiles, images = arrange_tiles(list(tiles.keys()), [], [])
ans1 = tiles[0][0] * tiles[0][N - 1] * tiles[N - 1][0] * tiles[N - 1][N - 1]
print(f"part 1: {ans1}")

# assemble actual image by removing borders
image_actual = []
for r in range(N):
    for rr in range(1, len(images[0][0]) - 1):
        for c in range(N):
            if c == 0:
                image_actual += [[]]
            image_actual[-1].extend(images[r][c][rr][1:-1])
R = C = len(image_actual)


def image_contains_sea_monster(image, r, c, sea_monster):
    """Checks whether an image contains a sea monster at a given position."""
    if r + len(sea_monster) > len(image) or c + len(sea_monster[0]) > len(image[0]):
        return False
    for rr in range(len(sea_monster)):
        for cc in range(len(sea_monster[0])):
            if sea_monster[rr][cc] == "#" and image[r + rr][c + cc] != "#":
                return False
    return True


water = [[image_actual[r][c] == "#" for c in range(C)] for r in range(R)]
for v in range(8):
    sea_monster = version(SEA_MONSTER, v)
    for r in range(R):
        for c in range(C):
            if image_contains_sea_monster(image_actual, r, c, sea_monster):
                for rr in range(len(sea_monster)):
                    for cc in range(len(sea_monster[0])):
                        if sea_monster[rr][cc] == "#":
                            water[r + rr][c + cc] = False
ans2 = sum(water[r][c] for r in range(R) for c in range(C))
print(f"part 2: {ans2}")

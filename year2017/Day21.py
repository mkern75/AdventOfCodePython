from utils import load_lines, tic, toc

INPUT_FILE = "./year2017/data/day21.txt"


def flip_vertical(image):
    R, C = len(image), len(image[0])
    image_flipped = [["." for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            image_flipped[r][c] = image[r][C - 1 - c]
    return image_flipped


def rotate_anticlockwise(image):
    R, C = len(image), len(image[0])
    image_rotated = [["." for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            image_rotated[r][c] = image[c][R - 1 - r]
    return image_rotated


def image_to_str(image):
    s = ""
    for r in range(len(image)):
        s += "".join(image[r])
        if r < len(image) - 1:
            s += "/"
    return s


def str_to_image(s):
    return [[c for c in row] for row in s.split("/")]


def load_rules(filename):
    rules = {}
    for line in load_lines(filename):
        fr, to = line.split(" => ")
        for t in range(8):  # save 2x4=8 different variants of flipping+rotating
            square_image = str_to_image(fr)
            if t // 4 == 1:
                square_image = flip_vertical(square_image)
            for i in range(t % 4):
                square_image = rotate_anticlockwise(square_image)
            rules[image_to_str(square_image)] = to
    return rules


def get_square(image, square_dim, sr, sc):
    square = [["." for _ in range(square_dim)] for _ in range(square_dim)]
    for r in range(square_dim):
        for c in range(square_dim):
            square[r][c] = image[sr * square_dim + r][sc * square_dim + c]
    return square


def get_enhanced_square(square, rules):
    return str_to_image(rules[image_to_str(square)])


def enhance(image, rules):
    image_dim = len(image)
    square_dim = 2 if image_dim % 2 == 0 else 3
    square_dim_new = square_dim + 1
    image_dim_new = image_dim // square_dim * square_dim_new
    image_new = [["." for _ in range(image_dim_new)] for _ in range(image_dim_new)]

    for sr in range(len(image) // square_dim):
        for sc in range(len(image) // square_dim):
            square = get_square(image, square_dim, sr, sc)
            square_new = get_enhanced_square(square, rules)
            for i in range(square_dim_new):
                for j in range(square_dim_new):
                    image_new[sr * square_dim_new + i][sc * square_dim_new + j] = square_new[i][j]

    return image_new


tic()
rules = load_rules(INPUT_FILE)

image = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
for i in range(5):
    image = enhance(image, rules)
ans1 = sum([1 for c in range(len(image[0])) for r in range(len(image)) if image[r][c] == "#"])
print(f"part 1: {ans1}  ({toc():.3f}s)")

tic()
image = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
for i in range(18):
    image = enhance(image, rules)
ans2 = sum([1 for c in range(len(image[0])) for r in range(len(image)) if image[r][c] == "#"])
print(f"part 2: {ans2}  ({toc():.3f}s)")

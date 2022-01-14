from utils import load_line
from colorama import Back, Style

INPUT_FILE = "./year2019/data/day08.txt"
R, C = 6, 25


def load_image(filename):
    inp = load_line(filename)
    L = len(inp) // (R * C)
    image = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for i in range(len(inp)):
        image[i // (C * R)][i % (C * R) // C][i % C] = int(inp[i])
    return image


def count_digit(digit, layer):
    cnt = 0
    for row in range(R):
        for col in range(C):
            if layer[row][col] == digit:
                cnt += 1
    return cnt


def pixel(row, col, image):
    for layer in range(len(image)):
        if image[layer][row][col] != 2:
            return image[layer][row][col]
    return 2


image = load_image(INPUT_FILE)

layer_min, min0 = -1, R * C + 1
for layer in range(len(image)):
    l0 = count_digit(0, image[layer])
    if l0 < min0:
        min0 = l0
        layer_min = layer
print("part 1:", count_digit(1, image[layer_min]) * count_digit(2, image[layer_min]))

print("part 2:")
for row in range(R):
    for col in range(C):
        if pixel(row, col, image) == 1:
            print(Back.GREEN + "X" + Style.RESET_ALL, end="")
        else:
            print(" ", end="")
    print()

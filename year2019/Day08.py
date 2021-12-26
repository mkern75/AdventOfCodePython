file = open("./year2019/data/day08.txt", "r")
lines = [line.rstrip('\n') for line in file]

C = 25
R = 6
L = len(lines[0]) // (R * C)


def load_image(inp):
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
    for layer in range(L):
        if image[layer][row][col] != 2:
            return image[layer][row][col]
    return 2


image = load_image(lines[0])

layer_min, min0 = -1, R * C + 1
for layer in range(L):
    l0 = count_digit(0, image[layer])
    if l0 < min0:
        min0 = l0
        layer_min = layer
print("part 1:", count_digit(1, image[layer_min]) * count_digit(2, image[layer_min]))

print("part 2:")
for row in range(R):
    for col in range(C):
        if pixel(row, col, image) == 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()

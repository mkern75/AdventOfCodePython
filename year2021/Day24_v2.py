file = open("./year2021/data/day24.txt", "r")
program = [line.rstrip('\n') for line in file]

# - basic idea: 14 blocks of repeating code; only differences are values in lists A, B, C
# - A[i] == 1 means register z is multiplied by 26: z = z * 26 + something
# - to offset that, the corresponing A[j] == 26 has to do a matching z = z // 26
# - corresponding positions are determined by a stack-like push/pop operation
# - for this to happen, the following has to be true: INPUT[i] + C[i] + B[j] = INPUT[j]
# - choose inputs so that both INPUT[i] and INPUT[j] are valid (1 to 9) and the overall number is maximised or minimised

A, B, C = [], [], []
for i in range(14):
    A += [int(program[i * 18 + 4].split()[2])]
    B += [int(program[i * 18 + 5].split()[2])]
    C += [int(program[i * 18 + 15].split()[2])]

matching_positions = []
for i in range(14):
    if A[i] == 1:
        c = 0
        for j in range(i, 14):
            c += 1 if A[j] == 1 else -1
            if c == 0:
                matching_positions += [(i, j)]
                break

number = [0] * 14
for (i, j) in matching_positions:
    for d in range(1, 10):
        if 1 <= d + C[i] + B[j] <= 9:
            number[i] = d
            number[j] = d + C[i] + B[j]
print("part 1:", "".join([str(n) for n in number]))

for (i, j) in matching_positions:
    for d in range(9, 0, -1):
        if 1 <= d + C[i] + B[j] <= 9:
            number[i] = d
            number[j] = d + C[i] + B[j]
print("part 2:", "".join([str(n) for n in number]))

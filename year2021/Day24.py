from datetime import datetime
import math

file = open("./year2021/data/day24.txt", "r")
program = [line.rstrip('\n') for line in file]

MAX_MODEL_NUMBER = 0
MIN_MODEL_NUMBER = math.inf

A, B, C = [], [], []
for i in range(14):
    A += [int(program[i * 18 + 4].split()[2])]
    B += [int(program[i * 18 + 5].split()[2])]
    C += [int(program[i * 18 + 15].split()[2])]


def reverse_one_block(z_out, a, b, c):
    result = []
    for single_input in range(1, 10):
        for i in range(0, a):
            z_in = a * z_out + i
            if z_in % 26 == single_input - b:
                result += [(single_input, z_in)]
        if z_out - single_input - c >= 0:
            if (z_out - single_input - c) % 26 == 0:
                for i in range(0, a):
                    z_in = (z_out - single_input - c) // 26 * a + i
                    if z_in % 26 != single_input - b:
                        result += [(single_input, z_in)]
    return result


def search_model_numbers(z_out, inputs):
    n = len(inputs)

    if n == 14:
        if z_out == 0:
            num = int("".join([str(n) for n in inputs]))
            global MIN_MODEL_NUMBER, MAX_MODEL_NUMBER
            MIN_MODEL_NUMBER = min(MIN_MODEL_NUMBER, num)
            MAX_MODEL_NUMBER = max(MAX_MODEL_NUMBER, num)
        return

    for (single_input, z_in) in reverse_one_block(z_out, A[13 - n], B[13 - n], C[13 - n]):
        new_inputs = [single_input] + inputs
        search_model_numbers(z_in, new_inputs)


print("start :", datetime.now().strftime("%H:%M:%S.%f"))
search_model_numbers(0, [])
print("part 1:", MAX_MODEL_NUMBER)
print("part 2:", MIN_MODEL_NUMBER)
print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

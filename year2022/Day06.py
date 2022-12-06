INPUT_FILE = "./year2022/data/day06.txt"
signal = [line.rstrip('\n') for line in open(INPUT_FILE, "r")][0]


def find_start(signal, n_unique_chars):
    for i in range(n_unique_chars, len(signal)):
        if len(set(signal[i - n_unique_chars:i])) == n_unique_chars:
            return i


print(f"part 1: {find_start(signal, 4)}")
print(f"part 2: {find_start(signal, 14)}")

INPUT_FILE = "./year2019/data/day16.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
signal_init = data[0]

PATTERN = [0, 1, 0, -1]


def flawed_frequency_transmission(signal, from_index=0):
    n = len(signal)
    signal_new = [0] * (n - 1) + [signal[n - 1]]
    # bottom half is fast
    for i in range(n - 2, max(n // 2, from_index) - 1, -1):
        signal_new[i] = (signal_new[i + 1] + signal[i]) % 10
    # top half is much slower
    for i in range(from_index, n // 2):
        signal_new[i] = abs(sum(PATTERN[((j + 1) % ((i + 1) * 4)) // (i + 1)] * signal[j] for j in range(n))) % 10
    return signal_new


# part 1
signal = [int(i) for i in signal_init]
for _ in range(100):
    signal = flawed_frequency_transmission(signal)
ans1 = "".join(str(i) for i in signal[:8])
print(f"part 1: {ans1}")

# part 2
offset = int(signal_init[:7])
signal = [int(i) for _ in range(10_000) for i in signal_init]
for _ in range(100):
    signal = flawed_frequency_transmission(signal, offset)
ans2 = "".join(str(i) for i in signal[offset:offset + 8])
print(f"part 2: {ans2}")

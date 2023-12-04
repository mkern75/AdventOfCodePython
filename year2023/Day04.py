INPUT_FILE = "./year2023/data/day04.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
N = len(data)

ans1, ans2 = 0, 0

n_cards = [1] * N
for i, line in enumerate(data):
    ans2 += n_cards[i]
    winning, own = [set(map(int, x.split())) for x in line.split(":")[1].split("|")]
    n_match = len(own & winning)
    if n_match:
        ans1 += 2 ** (n_match - 1)
        for j in range(n_match):
            n_cards[i + 1 + j] += n_cards[i]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

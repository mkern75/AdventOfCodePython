INPUT_FILE = "./year2023/data/day04.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
N = len(data)

ans1, ans2 = 0, 0

n_cards = [1] * N

for i, line in enumerate(data):
    ans2 += n_cards[i]
    x, y = line.split(":")[1].split("|")
    winning = set(map(int, x.split()))
    have = set(map(int, y.split()))
    match = have.intersection(winning)
    if match:
        ans1 += 2 ** (len(match) - 1)
        for j in range(len(match)):
            n_cards[i + 1 + j] += n_cards[i]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

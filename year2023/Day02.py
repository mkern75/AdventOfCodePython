import re

INPUT_FILE = "./year2023/data/day02.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

for line in data:
    header, info = line.split(":")
    game_id = int(header.split()[1])
    picks = re.split(r"[;,]", info)
    possible = True
    max_cnt = {"g": 0, "r": 0, "b": 0}
    for pick in picks:
        cnt, col = pick.split()
        cnt, col = int(cnt), col[0]
        if not (col == "r" and cnt <= 12 or col == "g" and cnt <= 13 or col == "b" and cnt <= 14):
            possible = False
        max_cnt[col] = max(max_cnt[col], cnt)
    if possible:
        ans1 += game_id
    ans2 += max_cnt["r"] * max_cnt["g"] * max_cnt["b"]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

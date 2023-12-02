import re

INPUT_FILE = "./year2023/data/day02.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

for game_id, line in enumerate(data, 1):
    max_cnt = {"g": 0, "r": 0, "b": 0}
    picks = re.split(r"[;,]", line.split(":")[1])
    for pick in picks:
        cnt, col = pick.split()
        cnt, col = int(cnt), col[0]
        max_cnt[col] = max(max_cnt[col], cnt)
    if max_cnt["r"] <= 12 and max_cnt["g"] <= 13 and max_cnt["b"] <= 14:
        ans1 += game_id
    ans2 += max_cnt["r"] * max_cnt["g"] * max_cnt["b"]

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

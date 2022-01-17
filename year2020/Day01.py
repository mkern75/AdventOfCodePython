from utils import load_numbers
from itertools import combinations

INPUT_FILE = "./year2020/data/day01.txt"

n = load_numbers(INPUT_FILE)

for c in combinations(n, 2):
    if c[0] + c[1] == 2020:
        ans1 = c[0] * c[1]
print("part 1:", ans1)

for c in combinations(n, 3):
    if c[0] + c[1] + c[2] == 2020:
        ans2 = c[0] * c[1] * c[2]
print("part 2:", ans2)

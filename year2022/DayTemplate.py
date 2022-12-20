import utils
import re
from collections import defaultdict, deque, Counter
from functools import lru_cache

INPUT_FILE = "./year2022/data/day20test.txt"
# INPUT_FILE = "./year2022/data/day20.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
# lines = utils.load_lines(INPUT_FILE)
# words = utils.load_words(INPUT_FILE)
# nums = utils.load_numbers(INPUT_FILE)
# grid = utils.load_grid(INPUT_FILE)
# grid = utils.load_int_grid(INPUT_FILE)
# R, C = len(grid), len(grid[0])
# blocks = utils.load_text_blocks()

ans1, ans2 = 0, 0

for line in data:
    pass

# for r in range(R):
#     for c in range(C):
#         pass

print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

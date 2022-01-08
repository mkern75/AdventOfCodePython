from utils import load_lines
from collections import Counter, namedtuple
import re

INPUT_FILE = "./year2018/data/day03.txt"
Claim = namedtuple("claim", "id left top width height")

claims = []
for line in load_lines(INPUT_FILE):
    m = re.compile(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)").match(line)
    claims += [Claim(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))]

fabric = Counter()
for claim in claims:
    for x in range(claim.left, claim.left + claim.width):
        for y in range(claim.top, claim.top + claim.height):
            fabric[(x, y)] += 1
ans1 = sum([1 for xy in fabric if fabric[xy] > 1])
print("part 1:", ans1)

for claim in claims:
    overlap = False
    for x in range(claim.left, claim.left + claim.width):
        for y in range(claim.top, claim.top + claim.height):
            if fabric[(x, y)] > 1:
                overlap = True
    if not overlap:
        print("part 2:", claim.id)
        break

from utils import load_lines
from collections import namedtuple
import re

INPUT_FILE = "./year2020/data/day02.txt"
Rule = namedtuple("password_rule", "low high letter password")

rules = []
for line in load_lines(INPUT_FILE):
    m = re.compile(r"([0-9]+)-([0-9]+) ([a-z]+): (.*)").match(line)
    rules += [Rule(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))]

ans1 = 0
for rule in rules:
    if rule.low <= rule.password.count(rule.letter) <= rule.high:
        ans1 += 1
print("part 1:", ans1)

ans2 = 0
for rule in rules:
    if (rule.password[rule.low - 1] == rule.letter and rule.password[rule.high - 1] != rule.letter) or (
            rule.password[rule.low - 1] != rule.letter and rule.password[rule.high - 1] == rule.letter):
        ans2 += 1
print("part 2:", ans2)

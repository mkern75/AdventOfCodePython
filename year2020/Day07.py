import re

INPUT_FILE = "./year2020/data/day07.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

rules = {}
for line in data:
    outer, content = re.match(r"(.*) bags contain (.*)\.", line).groups()
    rules[outer] = {}
    if content != "no other bags":
        for s in content.split(", "):
            cnt, inner = re.match(r"(\d+) (.*) bag", s).groups()
            rules[outer][inner] = int(cnt)


def inner_colours(outer):
    return set(rules[outer].keys()) | set().union(*(inner_colours(c) for c in rules[outer].keys()))


def n_inner_bags(outer):
    return 0 if len(rules[outer]) == 0 else sum(cnt + cnt * n_inner_bags(inner) for inner, cnt in rules[outer].items())


ans1 = sum(1 for outer in rules if "shiny gold" in inner_colours(outer))
print(f"part 1: {ans1}")

ans2 = n_inner_bags("shiny gold")
print(f"part 2: {ans2}")

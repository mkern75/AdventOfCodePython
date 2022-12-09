import re
from collections import Counter

INPUT_FILE = "./year2020/data/day21.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ingred_counter = Counter()  # counts the ingredients
allerg_options = {}  # maps allergens to their potential ingredients
for line in data:
    reg = re.match(r"(.*) \(contains (.*)\)", line)
    ingred = reg.groups()[0].split()
    allerg = reg.groups()[1].split(", ")
    ingred_counter.update(ingred)
    for a in allerg:
        if a not in allerg_options:
            allerg_options[a] = set(ingred)
        else:
            allerg_options[a] &= set(ingred)

ingred_to_allerg = {}
while any(a for a in allerg_options if len(allerg_options[a]) >= 1):
    a, (i,) = next((a, i) for a, i in allerg_options.items() if len(i) == 1)
    ingred_to_allerg[i] = a
    for a in allerg_options:
        if i in allerg_options[a]:
            allerg_options[a].remove(i)

ans1 = sum(ingred_counter[i] for i in ingred_counter if i not in ingred_to_allerg)
print(f"part 1: {ans1}")

ans2 = ",".join(sorted(list(ingred_to_allerg.keys()), key=lambda i: ingred_to_allerg[i]))
print(f"part 2: {ans2}")

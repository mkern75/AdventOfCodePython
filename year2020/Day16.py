import re
from math import prod

INPUT_FILE = "./year2020/data/day16.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

segments = [[]]
for line in data:
    if line != "":
        segments[-1] += [line]
    else:
        segments += [[]]

rules = []
for line in segments[0]:
    grps = re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
    rules += [(grps[0],) + tuple(map(int, grps[1:]))]
ticket_you = tuple(map(int, segments[1][1].split(",")))
tickets_nearby = [tuple(map(int, line.split(","))) for line in segments[2][1:]]
n_fields = len(ticket_you)


def is_valid(val, rule):
    return rule[1] <= val <= rule[2] or rule[3] <= val <= rule[4]


def is_invalid_value(val):
    return not any(is_valid(val, rule) for rule in rules)


def is_invalid_ticket(ticket):
    return any(is_invalid_value(val) for val in ticket)


# part 1
ans1 = sum(val for ticket in tickets_nearby for val in ticket if is_invalid_value(val))
print(f"part 1: {ans1}")

# part 2
tickets = [t for t in tickets_nearby if not is_invalid_ticket(t)]

candidates = []
for i in range(n_fields):
    candidates += [[rule[0] for rule in rules if all(is_valid(ticket[i], rule) for ticket in tickets)]]

field_order = [""] * n_fields
while any(len(c) > 0 for c in candidates):
    pos, field = next((i, c[0]) for i, c in enumerate(candidates) if len(c) == 1)
    field_order[pos] = field
    for c in candidates:
        if field in c:
            c.remove(field)

ans2 = prod(ticket_you[i] for i in range(n_fields) if field_order[i].startswith("departure"))
print(f"part 2: {ans2}")

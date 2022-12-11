import re

INPUT_FILE = "./year2020/data/day19.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
split = data.index("")
data_rules, messages = data[:split], data[split + 1:]

RULES = {}
for line in data_rules:
    rule_id, right = line.split(": ")
    rule_id = int(rule_id)
    if reg := re.match(r"\"([a-z])\"", right):
        RULES[rule_id] = reg.groups()[0]
    else:
        RULES[rule_id] = []
        for part in right.split(" | "):
            RULES[rule_id] += [list(map(int, part.split(" ")))]


def check_match(rules, text):
    if rules == [] and text == "":
        return True
    elif rules == [] or text == "":
        return False
    elif len(rules) > len(text):
        return False
    elif type(RULES[rules[0]]) == str:
        return check_match(rules[1:], text[1:]) if RULES[rules[0]] == text[0] else False
    else:
        for sub_rule in RULES[rules[0]]:
            if check_match(sub_rule + rules[1:], text):
                return True
        return False


# part 1
ans1 = sum(check_match([0], message) for message in messages)
print(f"part 1: {ans1}")

# part 2
RULES[8] = [[42], [42, 8]]
RULES[11] = [[42, 31], [42, 11, 31]]
ans2 = sum(check_match([0], message) for message in messages)
print(f"part 2: {ans2}")

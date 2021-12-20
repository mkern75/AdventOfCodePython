import re
from collections import Counter

file = open("./year2016/data/day04.txt", "r")
lines = [line.rstrip('\n') for line in file]


def check(line):
    m = re.compile("([a-z\-]*)-([0-9]+)\[([a-z]*)\]").match(line)
    encrypted_name = m.group(1)
    sector_id = int(m.group(2))
    checksum = m.group(3)
    chars = [c for c in encrypted_name if c != "-"]
    chars.sort()
    for i, (c, _) in enumerate(Counter(chars).most_common(5)):
        if checksum[i] != c:
            return False, None, None
    decrypted_name = ""
    for c in encrypted_name:
        decrypted_name += " " if c == "-" else chr((ord(c) - ord("a") + sector_id) % 26 + ord("a"))
    return True, sector_id, decrypted_name


ans1, ans2 = 0, 0
for line in lines:
    real, sector_id, message = check(line)
    if real:
        ans1 += sector_id
        if message == "northpole object storage":
            ans2 = sector_id
print(ans1)
print(ans2)

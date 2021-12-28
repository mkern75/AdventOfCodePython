from datetime import datetime

INPUT_FILE = "./year2016/data/day16.txt"


def dragon(s, l):
    if len(s) >= l:
        return s[:l]
    ss = s + "0"
    for i in range(len(s) - 1, -1, -1):
        ss += "1" if s[i] == "0" else "0"
    return dragon(ss, l)


def checksum(s):
    cs = ""
    for i in range(0, len(s) - 1, 2):
        cs += "1" if s[i:i + 2] in ["00", "11"] else "0"
    return cs if len(cs) % 2 == 1 else checksum(cs)


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

initial_state = lines[0]

ans1 = checksum(dragon(initial_state, 272))
print("part 1:", ans1)

ans2 = checksum(dragon(initial_state, 35651584))
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

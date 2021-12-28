from datetime import datetime

INPUT_FILE = "./year2016/data/day21.txt"


def swap_pos(pw, i, j):
    new_pw = pw.copy()
    c = new_pw[i]
    new_pw[i] = new_pw[j]
    new_pw[j] = c
    return new_pw


def swap_chars(pw, x, y):
    new_pw = []
    for c in pw:
        if c == x:
            new_pw += [y]
        elif c == y:
            new_pw += [x]
        else:
            new_pw += [c]
    return new_pw


def rotate_left(pw, r):
    r = r % len(pw)
    return pw[r:] + pw[:r]


def rotate_right(pw, r):
    r = r % len(pw)
    return pw[-r:] + pw[:-r]


def rotate(pw, x):
    i = pw.index(x)
    c = 1 + i if i < 4 else 2 + i
    return rotate_right(pw, c)


def rotate_reverse(pw, x):
    idx = pw.index(x)
    for i in range(len(pw)):
        c = 1 + i if i < 4 else 2 + i
        if (i + c) % len(pw) == idx:
            return rotate_left(pw, c)


def reverse(pw, i, j):
    return pw[:i] + pw[i:j + 1:][::-1] + pw[j + 1:]


def move(pw, i, j):
    c = pw[i]
    tmp_pw = pw[:i] + pw[i + 1:]
    return tmp_pw[:j] + [c] + tmp_pw[j:]


def apply(pw, op):
    s = op.split()
    if s[0] == "swap" and s[1] == "position":
        return swap_pos(pw, int(s[2]), int(s[5]))
    elif s[0] == "swap" and s[1] == "letter":
        return swap_chars(pw, s[2], s[5])
    elif s[0] == "rotate" and s[1] == "left":
        return rotate_left(pw, int(s[2]))
    elif s[0] == "rotate" and s[1] == "right":
        return rotate_right(pw, int(s[2]))
    elif s[0] == "reverse":
        return reverse(pw, int(s[2]), int(s[4]))
    elif s[0] == "move":
        return move(pw, int(s[2]), int(s[5]))
    elif s[0] == "rotate" and s[1] == "based":
        return rotate(pw, s[6])


def unapply(pw, op):
    s = op.split()
    if s[0] == "swap" and s[1] == "position":
        return swap_pos(pw, int(s[2]), int(s[5]))
    elif s[0] == "swap" and s[1] == "letter":
        return swap_chars(pw, s[2], s[5])
    elif s[0] == "rotate" and s[1] == "left":
        return rotate_right(pw, int(s[2]))
    elif s[0] == "rotate" and s[1] == "right":
        return rotate_left(pw, int(s[2]))
    elif s[0] == "reverse":
        return reverse(pw, int(s[2]), int(s[4]))
    elif s[0] == "move":
        return move(pw, int(s[5]), int(s[2]))
    elif s[0] == "rotate" and s[1] == "based":
        return rotate_reverse(pw, s[6])


def scramble(password, operations):
    pw = list(password)
    for op in operations:
        pw = apply(pw, op)
    return "".join(pw)


def unscramble(password, operations):
    pw = list(password)
    for op in reversed(operations):
        pw = unapply(pw, op)
    return "".join(pw)


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
operations = [line.rstrip('\n') for line in file]

ans1 = scramble("abcdefgh", operations)
print("part 1:", ans1)

ans2 = unscramble("fbgdceah", operations)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

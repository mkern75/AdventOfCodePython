def next_char(c):
    return chr(ord(c) + 1)


def inc_string(s):
    if s[-1] != "z":
        return s[:-1] + next_char(s[-1])
    else:
        return inc_string(s[:-1]) + "a"


def check_password(pw):
    ok = False
    for i in range(len(pw) - 2):
        if next_char(pw[i]) == pw[i + 1] and next_char(pw[i + 1]) == pw[i + 2]:
            ok = True
    if not ok:
        return False
    if pw.count("i") > 0 or pw.count("o") > 0 or pw.count("l") > 0:
        return False
    ok = False
    for i in range(len(pw) - 3):
        for j in range(i + 2, len(pw) - 1):
            if pw[i] == pw[i + 1] and pw[j] == pw[j + 1]:
                ok = True
    return ok


pw = "hepxcrrq"  # input
for i in range(2):
    while True:
        pw = inc_string(pw)
        if check_password(pw):
            break
    print(pw)

file = open("./year2016/data/day07.txt", "r")
lines = [line.rstrip('\n') for line in file]


def abba(s, i):
    return s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]


def aba(s, i):
    return s[i] == s[i + 2] and s[i] != s[i + 1]


def bab(s, i, aba_set):
    return s[i] == s[i + 2] and s[i] != s[i + 1] and s[i + 1] + s[i] + s[i + 1] in aba_set


def tls(s):
    has_abba = False
    c = 0
    for i in range(len(s) - 3):
        c += 1 if s[i] == "[" else (-1 if s[i] == "]" else 0)
        if abba(s, i):
            if c > 0:
                return False
            else:
                has_abba = True
    return has_abba


def ssl(s):
    aba_set = set()
    c = 0
    for i in range(len(s) - 2):
        c += 1 if s[i] == "[" else (-1 if s[i] == "]" else 0)
        if c == 0 and aba(s, i):
            aba_set.add(s[i:i + 3])
    c = 0
    for i in range(len(s) - 2):
        c += 1 if s[i] == "[" else (-1 if s[i] == "]" else 0)
        if c > 0 and bab(s, i, aba_set):
            return True
    return False


ans1, ans2 = 0, 0
for s in lines:
    if tls(s):
        ans1 += 1
    if ssl(s):
        ans2 += 1
print("part 1:", ans1)
print("part 2:", ans2)

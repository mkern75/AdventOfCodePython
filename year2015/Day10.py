s = "3113322113"  # input

for step in range(1, 51):
    ss, p = "", 0
    while p < len(s):
        c = 1
        while p + c < len(s) and s[p + c] == s[p]:
            c += 1
        ss += str(c) + s[p]
        p += c
    s = ss
    if step in [40, 50]:
        print(len(s))

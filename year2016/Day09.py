file = open("./year2016/data/day09.txt", "r")
lines = [line.rstrip('\n') for line in file]


def decompress_p1(s):
    res = ""
    pos = 0
    while pos < len(s):
        c = s[pos]
        if c == "(":
            start = pos + 1
            while s[pos] != ")":
                pos += 1
            end = pos
            a, b = list(map(int, s[start:end].split("x")))
            pos += 1
            for i in range(b):
                res += s[pos:pos + a]
            pos += a
        else:
            res += c
            pos += 1
    return res


def length_decompress_p2(s):
    res = 0
    pos = 0
    while pos < len(s):
        c = s[pos]
        if c == "(":
            start = pos + 1
            while s[pos] != ")":
                pos += 1
            end = pos
            a, b = list(map(int, s[start:end].split("x")))
            pos += 1
            res += b * length_decompress_p2(s[pos:pos + a])
            pos += a
        else:
            res += 1
            pos += 1
    return res


ans1 = len(decompress_p1(lines[0]))
print("part 1:", ans1)

ans2 = length_decompress_p2(lines[0])
print("part 2:", ans2)

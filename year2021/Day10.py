file = open("./data/year2021/day10.txt", "r")
lines = [line.rstrip('\n') for line in file]

m = {"(": ")", "[": "]", "{": "}", "<": ">"}
c1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
c2 = {")": 1, "]": 2, "}": 3, ">": 4}
e = 0
sc = []

for line in lines:
    st = []
    for c in line:
        if c in m:
            st.append(m[c])
        elif c == st[-1]:
            st.pop()
        else:
            e += c1[c]
            break
    else:
        s = 0
        while len(st) > 0:
            s = s * 5 + c2[st.pop()]
        sc.append(s)
sc.sort()
print(e)
print(sc[len(sc) // 2])

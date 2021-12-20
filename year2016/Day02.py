file = open("./year2016/data/day02.txt", "r")
lines = [line.rstrip('\n') for line in file]

ans1 = ""
r, c = 1, 1
for line in lines:
    for instr in line:
        if instr == "U" and r > 0:
            r -= 1
        elif instr == "D" and r < 2:
            r += 1
        elif instr == "L" and c > 0:
            c -= 1
        elif instr == "R" and c < 2:
            c += 1
    ans1 += str(r * 3 + c + 1)
print(ans1)

keypad = ["..1..", ".234.", "56789", ".ABC.", "..D.."]
ans2 = ""
r, c = 2, 0
for line in lines:
    for instr in line:
        if instr == "U" and r > 0 and keypad[r - 1][c] != ".":
            r -= 1
        elif instr == "D" and r < 4 and keypad[r + 1][c] != ".":
            r += 1
        elif instr == "L" and c > 0 and keypad[r][c - 1] != ".":
            c -= 1
        elif instr == "R" and c < 4 and keypad[r][c + 1] != ".":
            c += 1
    ans2 += keypad[r][c]
print(ans2)

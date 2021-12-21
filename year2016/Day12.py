file = open("./year2016/data/day12.txt", "r")
instr = [line.rstrip('\n') for line in file]


def execute(instr, mem, pos):
    while 0 <= pos < len(instr):
        s = instr[pos].split()
        if s[0] == "cpy":
            if s[1] in ["a", "b", "c", "d"]:
                mem[s[2]] = mem[s[1]]
            else:
                mem[s[2]] = int(s[1])
            pos += 1
        elif s[0] == "inc":
            mem[s[1]] += 1
            pos += 1
        elif s[0] == "dec":
            mem[s[1]] -= 1
            pos += 1
        elif s[0] == "jnz":
            if s[1] in ["a", "b", "c", "d"]:
                if mem[s[1]] != 0:
                    pos += int(s[2])
                else:
                    pos += 1
            else:
                if int(s[1]) != 0:
                    pos += int(s[2])
                else:
                    pos += 1
    return mem


mem = {"a": 0, "b": 0, "c": 0, "d": 0}
pos = 0
execute(instr, mem, pos)
print("part 1:", mem["a"])

mem = {"a": 0, "b": 0, "c": 1, "d": 0}
pos = 0
execute(instr, mem, pos)
print("part 2:", mem["a"])

file = open("./year2015/data/day23.txt", "r")
commands = [line.rstrip('\n') for line in file]


def execute(command, line, mem):
    s = command.replace(",", "").split(" ")
    if s[0] == "hlf":
        mem[s[1]] //= 2
        return line + 1, mem
    elif s[0] == "tpl":
        mem[s[1]] *= 3
        return line + 1, mem
    elif s[0] == "inc":
        mem[s[1]] += 1
        return line + 1, mem
    elif s[0] == "jmp":
        return line + int(s[1]), mem
    elif s[0] == "jie":
        return line + (int(s[2]) if mem[s[1]] % 2 == 0 else 1), mem
    elif s[0] == "jio":
        return line + (int(s[2]) if mem[s[1]] == 1 else 1), mem
    else:
        assert False


line = 0
mem = {"a": 0, "b": 0}
while 0 <= line < len(commands):
    line, mem = execute(commands[line], line, mem)
print(mem["b"])

line = 0
mem = {"a": 1, "b": 0}
while 0 <= line < len(commands):
    line, mem = execute(commands[line], line, mem)
print(mem["b"])

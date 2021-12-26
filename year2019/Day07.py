from collections import defaultdict
from itertools import permutations

file = open("./year2019/data/day07.txt", "r")
lines = [line.rstrip('\n') for line in file]


class IntcodeComputer:
    def __init__(self, name, program):
        self.name = name
        self.mem = defaultdict()
        for i in range(len(program)):
            self.mem[i] = program[i]
        self.input = []
        self.output = []
        self.ip = 0
        self.inpp = 0
        self.finished = False

    def val(self, pmode, i, ip):
        while i > 1:
            pmode //= 10
            i -= 1
        if pmode % 10 == 0:
            return self.mem[self.mem[ip]]
        elif pmode % 10 == 1:
            return self.mem[ip]
        else:
            assert False, "wrong parameter mode"

    def run(self):
        while self.ip in self.mem:
            opcode, pmode = self.mem[self.ip] % 100, self.mem[self.ip] // 100
            if opcode == 1:  # add
                self.mem[self.mem[self.ip + 3]] = self.val(pmode, 1, self.ip + 1) + self.val(pmode, 2, self.ip + 2)
                self.ip += 4
            elif opcode == 2:  # multiply
                self.mem[self.mem[self.ip + 3]] = self.val(pmode, 1, self.ip + 1) * self.val(pmode, 2, self.ip + 2)
                self.ip += 4
            elif opcode == 3:  # input
                if len(self.input) <= self.inpp:
                    break
                self.mem[self.mem[self.ip + 1]] = self.input[self.inpp]
                self.inpp += 1
                self.ip += 2
            elif opcode == 4:  # output
                self.output += [self.val(pmode, 1, self.ip + 1)]
                self.ip += 2
            elif opcode == 5:  # jump-if-true
                if self.val(pmode, 1, self.ip + 1) != 0:
                    self.ip = self.val(pmode, 2, self.ip + 2)
                else:
                    self.ip += 3
            elif opcode == 6:  # jump-if-false
                if self.val(pmode, 1, self.ip + 1) == 0:
                    self.ip = self.val(pmode, 2, self.ip + 2)
                else:
                    self.ip += 3
            elif opcode == 7:  # less than
                if self.val(pmode, 1, self.ip + 1) < self.val(pmode, 2, self.ip + 2):
                    self.mem[self.mem[self.ip + 3]] = 1
                else:
                    self.mem[self.mem[self.ip + 3]] = 0
                self.ip += 4
            elif opcode == 8:  # equals
                if self.val(pmode, 1, self.ip + 1) == self.val(pmode, 2, self.ip + 2):
                    self.mem[self.mem[self.ip + 3]] = 1
                else:
                    self.mem[self.mem[self.ip + 3]] = 0
                self.ip += 4
            elif opcode == 99:
                self.finished = True
                break
            else:
                assert False, "wrong opcode"


def run_amplifiers(program, seq, loop=False):
    amplifier = []
    for i in range(5):
        amplifier += [IntcodeComputer(i, program)]
        amplifier[i].input += [seq[i]]
    output = 0
    while True:
        for i in range(5):
            amplifier[i].input += [output]
            amplifier[i].run()
            output = amplifier[i].output[-1]
        if not loop or amplifier[4].finished:
            return output


program = list(map(int, lines[0].split(",")))

ans1 = 0
for seq in permutations([0, 1, 2, 3, 4]):
    ans1 = max(ans1, run_amplifiers(program, seq))
print("part 1:", ans1)

program = list(map(int, lines[0].split(",")))
ans2 = 0
for seq in permutations([5, 6, 7, 8, 9]):
    ans2 = max(ans2, run_amplifiers(program, seq, True))
print("part 2:", ans2)

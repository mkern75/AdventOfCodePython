from collections import defaultdict


def mode(pmode, i):
    while i > 1:
        pmode //= 10
        i -= 1
    return pmode % 10


class IntcodeComputer:
    def __init__(self, program):
        self.memory = defaultdict(int)
        for i in range(len(program)):
            self.memory[i] = program[i]
        self.input = []
        self.output = []
        self.ip = 0  # instruction pointer
        self.inpp = 0  # input pointer
        self.rb = 0  # relative base
        self.finished = False

    def reset(self, program):
        self.memory = defaultdict(int)
        for i in range(len(program)):
            self.memory[i] = program[i]
        self.input = []
        self.output = []
        self.ip = 0
        self.inpp = 0
        self.rb = 0
        self.finished = False

    def read(self, pmode, ip):
        if pmode == 0:  # position mode
            return self.memory[self.memory[ip]]
        elif pmode == 1:  # immediate mode
            return self.memory[ip]
        elif pmode == 2:  # relative mode
            return self.memory[self.memory[ip] + self.rb]
        else:
            assert False, "unknown parameter mode"

    def write(self, pmode, ip, v):
        if pmode == 0:  # position mode
            self.memory[self.memory[ip]] = v
        elif pmode == 1:  # immediate mode
            assert False, "no write in immediate mode"
        elif pmode == 2:  # relative mode
            self.memory[self.memory[ip] + self.rb] = v
        else:
            assert False, "unknown parameter mode"

    def run(self):
        while self.ip in self.memory:
            opcode, pmode = self.memory[self.ip] % 100, self.memory[self.ip] // 100
            if opcode == 1:  # add
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                self.write(mode(pmode, 3), self.ip + 3, v1 + v2)
                self.ip += 4
            elif opcode == 2:  # multiply
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                self.write(mode(pmode, 3), self.ip + 3, v1 * v2)
                self.ip += 4
            elif opcode == 3:  # input
                if len(self.input) <= self.inpp:
                    break
                self.write(mode(pmode, 1), self.ip + 1, self.input[self.inpp])
                self.inpp += 1
                self.ip += 2
            elif opcode == 4:  # output
                self.output += [self.read(mode(pmode, 1), self.ip + 1)]
                self.ip += 2
            elif opcode == 5:  # jump-if-true
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                if v1 != 0:
                    self.ip = v2
                else:
                    self.ip += 3
            elif opcode == 6:  # jump-if-false
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                if v1 == 0:
                    self.ip = v2
                else:
                    self.ip += 3
            elif opcode == 7:  # less than
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                if v1 < v2:
                    self.write(mode(pmode, 3), self.ip + 3, 1)
                else:
                    self.write(mode(pmode, 3), self.ip + 3, 0)
                self.ip += 4
            elif opcode == 8:  # equals
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                v2 = self.read(mode(pmode, 2), self.ip + 2)
                if v1 == v2:
                    self.write(mode(pmode, 3), self.ip + 3, 1)
                else:
                    self.write(mode(pmode, 3), self.ip + 3, 0)
                self.ip += 4
            elif opcode == 9:  # relative base offset
                v1 = self.read(mode(pmode, 1), self.ip + 1)
                self.rb += v1
                self.ip += 2
            elif opcode == 99:
                self.finished = True
                break
            else:
                assert False, "wrong opcode"

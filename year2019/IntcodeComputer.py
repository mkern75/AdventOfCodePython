from collections import defaultdict


class IntcodeComputer:
    def __init__(self, program):
        self.memory = defaultdict()
        for i in range(len(program)):
            self.memory[i] = program[i]
        self.input = []
        self.output = []
        self.ip = 0
        self.inpp = 0
        self.finished = False

    def reset(self, program):
        self.memory = defaultdict()
        for i in range(len(program)):
            self.memory[i] = program[i]
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
            return self.memory[self.memory[ip]]
        elif pmode % 10 == 1:
            return self.memory[ip]
        else:
            assert False, "wrong parameter mode"

    def run(self):
        while self.ip in self.memory:
            opcode, pmode = self.memory[self.ip] % 100, self.memory[self.ip] // 100
            if opcode == 1:  # add
                self.memory[self.memory[self.ip + 3]] = self.val(pmode, 1, self.ip + 1) + self.val(pmode, 2, self.ip + 2)
                self.ip += 4
            elif opcode == 2:  # multiply
                self.memory[self.memory[self.ip + 3]] = self.val(pmode, 1, self.ip + 1) * self.val(pmode, 2, self.ip + 2)
                self.ip += 4
            elif opcode == 3:  # input
                if len(self.input) <= self.inpp:
                    break
                self.memory[self.memory[self.ip + 1]] = self.input[self.inpp]
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
                    self.memory[self.memory[self.ip + 3]] = 1
                else:
                    self.memory[self.memory[self.ip + 3]] = 0
                self.ip += 4
            elif opcode == 8:  # equals
                if self.val(pmode, 1, self.ip + 1) == self.val(pmode, 2, self.ip + 2):
                    self.memory[self.memory[self.ip + 3]] = 1
                else:
                    self.memory[self.memory[self.ip + 3]] = 0
                self.ip += 4
            elif opcode == 99:
                self.finished = True
                break
            else:
                assert False, "wrong opcode"

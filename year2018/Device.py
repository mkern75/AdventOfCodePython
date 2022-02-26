class Device:

    def __init__(self, program, debug=False):
        self.reg = [0] * 6
        self.ip = 0
        self.debug = debug
        if program[0].startswith("#ip"):
            self.ip_reg = int(program[0].split()[1])
            self.program = program[1:]
        else:
            self.ip_reg = None
            self.program = program

    def reset(self, program):
        self.reg = [0] * 6
        self.ip = 0
        if program[0].startswith("#ip"):
            self.ip_reg = int(program[0].split()[1])
            self.program = program[1:]
        else:
            self.ip_reg = None
            self.program = program

    def run(self):
        while 0 <= self.ip < len(self.program):
            self.run_one_cycle()

    def run_one_cycle(self):
        s = self.program[self.ip].split()
        if self.ip_reg is not None:
            self.reg[self.ip_reg] = self.ip
        op, a, b, c = s[0], int(s[1]), int(s[2]), int(s[3])
        if self.debug:
            print(f"ip={self.ip}", self.reg, op, a, b, c, end=" ")
        if op == "addr":
            self.reg[c] = self.reg[a] + self.reg[b]
        elif op == "addi":
            self.reg[c] = self.reg[a] + b
        elif op == "mulr":
            self.reg[c] = self.reg[a] * self.reg[b]
        elif op == "muli":
            self.reg[c] = self.reg[a] * b
        elif op == "banr":
            self.reg[c] = self.reg[a] & self.reg[b]
        elif op == "bani":
            self.reg[c] = self.reg[a] & b
        elif op == "borr":
            self.reg[c] = self.reg[a] | self.reg[b]
        elif op == "bori":
            self.reg[c] = self.reg[a] | b
        elif op == "setr":
            self.reg[c] = self.reg[a]
        elif op == "seti":
            self.reg[c] = a
        elif op == "gtir":
            self.reg[c] = 1 if a > self.reg[b] else 0
        elif op == "gtri":
            self.reg[c] = 1 if self.reg[a] > b else 0
        elif op == "gtrr":
            self.reg[c] = 1 if self.reg[a] > self.reg[b] else 0
        elif op == "eqir":
            self.reg[c] = 1 if a == self.reg[b] else 0
        elif op == "eqri":
            self.reg[c] = 1 if self.reg[a] == b else 0
        elif op == "eqrr":
            self.reg[c] = 1 if self.reg[a] == self.reg[b] else 0
        else:
            assert False
        if self.debug:
            print(self.reg)
        if self.ip_reg is not None:
            self.ip = self.reg[self.ip_reg]
        self.ip += 1

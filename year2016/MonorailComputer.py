class MonorailComputer:
    def __init__(self, program):
        self.program = program.copy()
        self.memory = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.ipp = 0  # instruction pointer

    def reset(self, program):
        self.program = program.copy()
        self.memory = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.ipp = 0  # instruction pointer

    def run(self):
        while 0 <= self.ipp < len(self.program):
            s = self.program[self.ipp].split()
            if s[0] == "cpy":
                if s[1] in ["a", "b", "c", "d"]:
                    self.memory[s[2]] = self.memory[s[1]]
                else:
                    self.memory[s[2]] = int(s[1])
                self.ipp += 1
            elif s[0] == "inc":
                self.memory[s[1]] += 1
                self.ipp += 1
            elif s[0] == "dec":
                self.memory[s[1]] -= 1
                self.ipp += 1
            elif s[0] == "jnz":
                if s[1] in ["a", "b", "c", "d"]:
                    if self.memory[s[1]] != 0:
                        self.ipp += int(s[2])
                    else:
                        self.ipp += 1
                else:
                    if int(s[1]) != 0:
                        self.ipp += int(s[2])
                    else:
                        self.ipp += 1

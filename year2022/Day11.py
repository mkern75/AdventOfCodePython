import re
import math

INPUT_FILE = "./year2022/data/day11.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
data_segments = [[]]
for line in data:
    if line == "":
        data_segments += [[]]
    else:
        data_segments[-1] += [line]


class Monkey:
    MONKEYS = {}  # internal dictionary to facilitate throwing of items to other monkeys
    MOD = 1  # for part 2, we only have to keep worry levels modulo MOD = (test_monkey_0 * ... test_monkey_n)

    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.initial_items = items
        self.items = [i for i in self.initial_items]
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0
        Monkey.MONKEYS[self.name] = self
        Monkey.MOD *= self.test

    def add_item(self, item):
        self.items += [item]

    def exec_turn(self, keep_worry_level_down=True):
        while self.items:
            item = self.items.pop(0)
            item = eval(self.operation.replace("old", str(item)))
            if keep_worry_level_down:
                item //= 3
            else:
                item = item % Monkey.MOD
            Monkey.MONKEYS[self.if_true if item % self.test == 0 else self.if_false].add_item(item)
            self.inspections += 1

    def reset(self):
        self.items = [i for i in self.initial_items]
        self.inspections = 0

    def __repr__(self):
        return f"monkey {self.name} with items {self.items} and {self.inspections} inspections"


# parse data
monkeys = []
for ds in data_segments:
    name = int(re.match(r"Monkey (\d+):", ds[0]).groups()[0])
    items = list(map(int, (re.search(r"Starting items: (.*)", ds[1]).groups()[0]).split(",")))
    operation = re.search(r"Operation: new = (.*)", ds[2]).groups()[0]
    test = int(re.search(r"Test: divisible by (.*)", ds[3]).groups()[0])
    if_true = int(re.search(r"If true: throw to monkey (\d+)", ds[4]).groups()[0])
    if_false = int(re.search(r"If false: throw to monkey (\d+)", ds[5]).groups()[0])
    monkeys += [Monkey(name, items, operation, test, if_true, if_false)]

# part 1
for _ in (range(20)):
    for monkey in monkeys:
        monkey.exec_turn()
ans1 = math.prod(x.inspections for x in sorted(monkeys, key=lambda m: -m.inspections)[:2])
print(f"part 1: {ans1}")

# part 2
for monkey in monkeys:
    monkey.reset()
for c in range(10_000):
    for monkey in monkeys:
        monkey.exec_turn(False)
ans2 = math.prod(x.inspections for x in sorted(monkeys, key=lambda m: -m.inspections)[:2])
print(f"part 2: {ans2}")

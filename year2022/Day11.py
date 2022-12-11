import re
import math

INPUT_FILE = "./year2022/data/day11.txt"
data = [[line.rstrip('\n') for line in p.splitlines()] for p in open(INPUT_FILE, "r").read().strip().split("\n\n")]


def load_monkeys(data):
    monkeys = []
    for segment in data:
        name = int(re.match(r"Monkey (\d+):", segment[0]).groups()[0])
        items = list(map(int, (re.search(r"Starting items: (.*)", segment[1]).groups()[0]).split(",")))
        operation = re.search(r"Operation: new = (.*)", segment[2]).groups()[0]
        divisibility_test = int(re.search(r"Test: divisible by (.*)", segment[3]).groups()[0])
        monkey_if_true = int(re.search(r"If true: throw to monkey (\d+)", segment[4]).groups()[0])
        monkey_if_false = int(re.search(r"If false: throw to monkey (\d+)", segment[5]).groups()[0])
        monkeys += [Monkey(name, items, operation, divisibility_test, monkey_if_true, monkey_if_false)]
    return monkeys


class Monkey:
    MONKEYS = {}  # internal dictionary to facilitate throwing of items to other monkeys
    MOD = 1  # for part 2, we only have to keep worry levels modulo MOD = (test_monkey_0 * ... test_monkey_n)

    def __init__(self, name, items, operation, divisibility_test, monkey_if_true, monkey_if_false):
        self.name = name
        self.initial_items = items
        self.items = [i for i in self.initial_items]
        self.operation = operation
        self.divisibility_test = divisibility_test
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.inspections = 0
        Monkey.MONKEYS[self.name] = self
        Monkey.MOD *= self.divisibility_test

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
            target = self.monkey_if_true if item % self.divisibility_test == 0 else self.monkey_if_false
            Monkey.MONKEYS[target].add_item(item)
            self.inspections += 1

    def reset(self):
        self.items = [i for i in self.initial_items]
        self.inspections = 0

    def __repr__(self):
        return f"monkey {self.name} with items {self.items} and {self.inspections} inspections"


# part 1
monkeys = load_monkeys(data)

for _ in (range(20)):
    for monkey in monkeys:
        monkey.exec_turn()
ans1 = math.prod(monkey.inspections for monkey in sorted(monkeys, key=lambda x: x.inspections)[-2:])
print(f"part 1: {ans1}")

# part 2
for monkey in monkeys:
    monkey.reset()

for c in range(10_000):
    for monkey in monkeys:
        monkey.exec_turn(False)
ans2 = math.prod(monkey.inspections for monkey in sorted(monkeys, key=lambda x: x.inspections)[-2:])
print(f"part 2: {ans2}")

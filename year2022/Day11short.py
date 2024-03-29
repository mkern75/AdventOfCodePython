from math import prod

INPUT_FILE = "./year2022/data/day11.txt"
data = [[line.rstrip('\n') for line in p.splitlines()] for p in open(INPUT_FILE).read().strip().split("\n\n")]


def load_monkeys(data):
    monkeys = []
    for i, d in enumerate(data):
        items = list(map(int, d[1].split(":")[-1].split(",")))
        op = d[2].split("= ")[-1]
        test = int(d[3].split()[-1])
        true = int(d[4].split()[-1])
        false = int(d[5].split()[-1])
        monkeys += [[i, items, op, test, true, false, 0]]
    return monkeys


def exec_one_round(monkeys, mod=None):
    for monkey in monkeys:
        while monkey[1]:
            item = monkey[1].pop(0)
            item = eval(monkey[2].replace("old", str(item)))
            item = item // 3 if mod is None else item % mod
            monkeys[monkey[4] if item % monkey[3] == 0 else monkey[5]][1].append(item)
            monkey[-1] += 1


# part 1
monkeys = load_monkeys(data)
for _ in range(20):
    exec_one_round(monkeys)
ans1 = prod(monkey[6] for monkey in sorted(monkeys, key=lambda m: -m[-1])[:2])
print(f"part 1: {ans1}")

# part 2
monkeys = load_monkeys(data)
mod = prod(monkey[3] for monkey in monkeys)
for _ in range(10_000):
    exec_one_round(monkeys, mod)
ans2 = prod(monkey[6] for monkey in sorted(monkeys, key=lambda m: -m[-1])[:2])
print(f"part 2: {ans2}")

from utils import load_numbers

INPUT_FILE = "./year2019/data/day01.txt"

modules = load_numbers(INPUT_FILE)
N = len(modules)

ans1 = 0
for module in modules:
    ans1 += max(module // 3 - 2, 0)
print("part 1:", ans1)

ans2 = 0
for module in modules:
    fuel = max(module // 3 - 2, 0)
    ans2 += fuel
    while fuel > 0:
        fuel = max(fuel // 3 - 2, 0)
        ans2 += fuel
print("part 2:", ans2)

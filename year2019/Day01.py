file = open("./year2019/data/day01.txt", "r")
modules = [int(line.rstrip('\n')) for line in file]
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

from utils import load_number, tic, toc

INPUT_FILE = "./year2018/data/day14.txt"

tic()
n = load_number(INPUT_FILE)
recipes = [3, 7]
elf1, elf2 = 0, 1

while len(recipes) < n + 10:
    recipes += [int(i) for i in str(recipes[elf1] + recipes[elf2])]
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
ans1 = "".join([str(i) for i in recipes[n:n + 10]])
print(f"part 1: {ans1}   ({toc():.3f}s)")

tic()
n = str(n)
recipes = [3, 7]
elf1, elf2 = 0, 1

while True:
    recipes += [int(i) for i in str(recipes[elf1] + recipes[elf2])]
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    if n == "".join([str(i) for i in recipes[-len(n):]]):
        print(f"part 2: {len(recipes) - len(n)}   ({toc():.3f}s)")
        break
    elif n == "".join([str(i) for i in recipes[-len(n) - 1:-1]]):
        print(f"part 2: {len(recipes) - len(n) - 1}   ({toc():.3f}s)")
        break

INPUT_FILE = "./year2022/data/day21.txt"
jobs = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

root = 0
while root == 0:
    for job in jobs:
        try:
            exec(job.replace(":", " =").replace("/", "//"))
        except:
            pass
print(f"part 1: {root}")

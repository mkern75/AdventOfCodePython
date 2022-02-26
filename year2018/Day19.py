from utils import load_lines, tic, toc
from Device import Device

INPUT_FILE = "./year2018/data/day19.txt"

tic()
program = load_lines(INPUT_FILE)

device = Device(program)
device.run()
print(f"part 1: {device.reg[0]}   ({toc():.3f}s)")

# Part 2 would run by far too long, so we analyse program instead:
#   a) a large number <n> is computed between program lines 17 to 33 and stored in register[2]
#   b) register[0] is reset to 0
#   c) all numbers from 1 to <n> that divide <n> are summed up in register[0]
# Solution: we only simulate the device for part a) to calculate <n>, and then calculate the rest directly (faster!).
tic()
device.reset(program)
device.reg[0] = 1
for i in range(1, 18):  # run the first 18 steps to get the large number from register[2]
    device.run_one_cycle()
n = device.reg[2]

ans2 = 0
for i in range(1, n + 1):
    if n % i == 0:
        ans2 += i
print(f"part 2: {ans2}   ({toc():.3f}s)")

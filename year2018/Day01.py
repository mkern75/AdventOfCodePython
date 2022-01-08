from utils import load_numbers

INPUT_FILE = "./year2018/data/day01.txt"

nums = load_numbers(INPUT_FILE)
print("part 1:", sum(nums))

freq = 0
hist = set()
i = 0
while freq not in hist:
    hist.add(freq)
    freq += nums[i]
    i = (i + 1) % len(nums)
print("part 2:", freq)

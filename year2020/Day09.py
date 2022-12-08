INPUT_FILE = "./year2020/data/day09.txt"
nums = [int(line.rstrip('\n')) for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0

for i in range(25, len(nums)):
    if not any(nums[i] == nums[i - j] + nums[i - k] for j in range(1, 25) for k in range(j + 1, 26)):
        ans1 = nums[i]
        print(f"part 1: {ans1}")
        break

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        s = sum(nums[i:j + 1])
        if sum(nums[i:j + 1]) == ans1:
            ans2 = min(nums[i:j + 1]) + max(nums[i:j + 1])
            print(f"part 2: {ans2}")
        elif s > ans1:
            break

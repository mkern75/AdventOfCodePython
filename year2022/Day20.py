INPUT_FILE = "./year2022/data/day20.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
N = len(data)


def single_move(nums, num):
    pos = nums.index(num)
    pos_new = (pos + num[0]) % (N - 1)
    if pos_new >= pos:
        return nums[:pos] + nums[pos + 1:pos_new + 1] + [num] + nums[pos_new + 1:]
    else:
        return nums[:pos_new] + [num] + nums[pos_new:pos] + nums[pos + 1:]


# part 1
orig = [(int(l), i) for i, l in enumerate(data)]
nums = [num for num in orig]
for num in orig:
    nums = single_move(nums, num)
zero = next(num for num in orig if num[0] == 0)
pzero = nums.index(zero)
ans1 = nums[(pzero + 1000) % N][0] + nums[(pzero + 2000) % N][0] + nums[(pzero + 3000) % N][0]
print(f"part 1: {ans1}")

# part 2
orig = [(int(l) * 811589153, i) for i, l in enumerate(data)]
nums = [num for num in orig]
for _ in range(10):
    for num in orig:
        nums = single_move(nums, num)
zero = next(num for num in orig if num[0] == 0)
pzero = nums.index(zero)
ans2 = nums[(pzero + 1000) % N][0] + nums[(pzero + 2000) % N][0] + nums[(pzero + 3000) % N][0]
print(f"part 2: {ans2}")

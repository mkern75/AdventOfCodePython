INPUT_FILE = "./year2022/data/day20.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
N = len(data)


def single_move(nums, num):
    idx = nums.index(num)
    idx_new = (idx + num[0]) % (N - 1)
    nums.remove(num)
    nums.insert(idx_new, num)


# part 1
orig = [(int(l), i) for i, l in enumerate(data)]
nums = [num for num in orig]
for num in orig:
    single_move(nums, num)
zero = next(num for num in orig if num[0] == 0)
idx_zero = nums.index(zero)
ans1 = nums[(idx_zero + 1000) % N][0] + nums[(idx_zero + 2000) % N][0] + nums[(idx_zero + 3000) % N][0]
print(f"part 1: {ans1}")

# part 2
orig = [(int(l) * 811589153, i) for i, l in enumerate(data)]
nums = [num for num in orig]
for _ in range(10):
    for num in orig:
        single_move(nums, num)
zero = next(num for num in orig if num[0] == 0)
idx_zero = nums.index(zero)
ans2 = nums[(idx_zero + 1000) % N][0] + nums[(idx_zero + 2000) % N][0] + nums[(idx_zero + 3000) % N][0]
print(f"part 2: {ans2}")

INPUT_FILE = "./year2022/data/day20.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]
N = len(data)


def mix(nums, order):
    for n in order:
        idx = nums.index(n)
        idx_new = (idx + n[0]) % (N - 1)
        nums.remove(n)
        nums.insert(idx_new, n)


def sum_of_grove_coordinates(nums):
    idx_zero = next(i for i, n in enumerate(nums) if n[0] == 0)
    return sum(nums[(idx_zero + 1000 * i) % N][0] for i in range(1, 4))


# part 1
orig = [(int(l), i) for i, l in enumerate(data)]
nums = [num for num in orig]
mix(nums, orig)
print(f"part 1: {sum_of_grove_coordinates(nums)}")

# part 2
orig = [(int(l) * 811589153, i) for i, l in enumerate(data)]
nums = [num for num in orig]
for _ in range(10):
    mix(nums, orig)
print(f"part 2: {sum_of_grove_coordinates(nums)}")

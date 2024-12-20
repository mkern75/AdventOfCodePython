from time import time

time_start = time()
INPUT_FILE = "./year2024/data/day07.txt"
data = [line.rstrip("\n") for line in open(INPUT_FILE, "r")]


def is_valid_original(result, numbers, part2=False):
    n = len(numbers)
    st = [(numbers[0], 1)]
    while st:
        r, i = st.pop()
        # all numbers are positive and thus the available operators cannot decrease the result
        if r > result:
            continue
        if i == n:
            if r == result:
                return True
            continue
        st.append((r + numbers[i], i + 1))
        st.append((r * numbers[i], i + 1))
        if part2:
            st.append((int(str(r) + str(numbers[i])), i + 1))
    return False


def is_valid(result, numbers, part2=False):
    st = [(result, len(numbers))]
    while st:
        r, i = st.pop()
        if i == 1:
            if r == numbers[0]:
                return True
            continue
        i -= 1
        if r >= numbers[i]:
            st.append((r - numbers[i], i))
        if r % numbers[i] == 0:
            st.append((r // numbers[i], i))
        if part2 and r > numbers[i]:
            rs, ns = str(r), str(numbers[i])
            if rs.endswith(ns):
                st.append((int(rs[:-len(ns)]), i))
    return False


ans1, ans2 = 0, 0
for line in data:
    res, other = line.split(":")
    res = int(res)
    nums = list(map(int, other.split()))
    if is_valid(res, nums, False):
        ans1 += res
        ans2 += res
    elif is_valid(res, nums, True):
        ans2 += res

print(f"part 1: {ans1}  ({time() - time_start:.3f}s)")
print(f"part 2: {ans2}  ({time() - time_start:.3f}s)")

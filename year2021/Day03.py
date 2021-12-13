file = open("./year2021/data/day03.txt", "r")
lines = [line.rstrip('\n').split(" ") for line in file]
bin_nums = [n for line in lines for n in line]
n_bits = len(bin_nums[0])


def get_bit(bin_nums, pos, is_max):
    bits = [n[pos] for n in bin_nums]
    c = bits.count("1")
    return ("1" if 2 * c >= len(bits) else "0") if is_max != 0 else ("1" if 2 * c < len(bits) else "0")


def filter_bin_nums(bin_nums, pos, is_max):
    if len(bin_nums) == 1:
        return bin_nums
    b = get_bit(bin_nums, pos, is_max)
    return list(filter(lambda x: x[pos] == b, bin_nums))


gamma, epsilon = "", ""
for pos in range(n_bits):
    gamma += get_bit(bin_nums, pos, 1)
    epsilon += get_bit(bin_nums, pos, 0)
power = int(gamma, 2) * int(epsilon, 2)
print(power)

ox, co2 = bin_nums, bin_nums
for pos in range(n_bits):
    ox = filter_bin_nums(ox, pos, 1)
    co2 = filter_bin_nums(co2, pos, 0)
support = int(ox[0], 2) * int(co2[0], 2)
print(support)

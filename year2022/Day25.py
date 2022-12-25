INPUT_FILE = "./year2022/data/day25.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

SNAFU_2_DEC = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DEC_2_SNAFU = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

dec = 0
for line in data:
    for exponent, snafu_digit in enumerate(reversed(line)):
        dec += SNAFU_2_DEC[snafu_digit] * 5 ** exponent

snafu = ""
while dec > 0:
    dec_digit = dec % 5
    if dec_digit > 2:
        dec_digit -= 5
    snafu = DEC_2_SNAFU[dec_digit] + snafu
    dec = (dec - dec_digit) // 5
print(f"part 1: {snafu}")

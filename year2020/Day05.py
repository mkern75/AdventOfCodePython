INPUT_FILE = "./year2020/data/day05.txt"
data = [line.rstrip('\n') for line in open(INPUT_FILE, "r")]

ans1, ans2 = 0, 0
occupied = set()
for line in data:
    row = sum(pow(2, 6 - i) for i in range(7) if line[i] == "B")
    col = sum(pow(2, 9 - i) for i in range(7, 10) if line[i] == "R")
    seat = row * 8 + col
    occupied |= {seat}
    ans1 = max(ans1, row * 8 + col)
for seat in occupied:
    if seat + 1 not in occupied and seat + 2 in occupied:
        ans2 = seat + 1
        break
print(f"part 1: {ans1}")
print(f"part 2: {ans2}")

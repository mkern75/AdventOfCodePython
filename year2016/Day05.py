import hashlib

file = open("./year2016/data/day05.txt", "r")
lines = [line.rstrip('\n') for line in file]

ans1 = ""
door, idx = lines[0], 0
while len(ans1) < 8:
    while not hashlib.md5((door + str(idx)).encode("utf-8")).hexdigest().startswith("00000"):
        idx += 1
    ans1 += hashlib.md5((door + str(idx)).encode("utf-8")).hexdigest()[5]
    idx += 1
print(ans1)

ans2 = "________"
door, idx, cnt = lines[0], 0, 0
while cnt < 8:
    while not hashlib.md5((door + str(idx)).encode("utf-8")).hexdigest().startswith("00000"):
        idx += 1
    p = hashlib.md5((door + str(idx)).encode("utf-8")).hexdigest()[5]
    if p in ["0", "1", "2", "3", "4", "5", "6", "7"]:
        p = int(p)
        if ans2[p] == "_":
            ans2 = ans2[:p] + hashlib.md5((door + str(idx)).encode("utf-8")).hexdigest()[6] + ans2[p + 1:]
            cnt += 1
    idx += 1
print(ans2)

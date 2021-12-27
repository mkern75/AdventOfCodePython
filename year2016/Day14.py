import hashlib
from datetime import datetime

INPUT_FILE = "./year2016/data/day14.txt"


def first_3x_char(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return None


def contains_char_5x(c, alist):
    for e in alist:
        if c * 5 in e:
            return True
    return False


def my_hash(s, depth):
    for i in range(depth):
        s = hashlib.md5(s.encode("utf-8")).hexdigest()
    return s


def index_nth_key(n, salt, hash_depth=1):
    idx, cnt, mem = 0, 0, []
    while True:
        mem += [my_hash(salt + str(idx), hash_depth)]
        if len(mem) == 1001:
            c = first_3x_char(mem[0])
            mem = mem[1:]
            if c is not None and contains_char_5x(c, mem):
                cnt += 1
                if cnt == n:
                    return idx - 1000
        idx += 1


print("start :", datetime.now().strftime("%H:%M:%S.%f"))

file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]
salt = lines[0]

ans1 = index_nth_key(64, salt)
print("part 1:", ans1)

ans2 = index_nth_key(64, salt, 2017)
print("part 2:", ans2)

print("finish:", datetime.now().strftime("%H:%M:%S.%f"))

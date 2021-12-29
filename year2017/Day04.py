import time

t0 = time.time()
INPUT_FILE = "./year2017/data/day04.txt"


def valid(words):
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                return False
    return True


def anagram(word1, word2):
    return "".join(sorted(word1)) == "".join(sorted(word2))


def valid2(words):
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if anagram(words[i], words[j]):
                return False
    return True


file = open(INPUT_FILE, "r")
lines = [line.rstrip('\n') for line in file]

ans1 = 0
for line in lines:
    ans1 += 1 if valid(list(line.split())) else 0
print("part 1:", ans1, f"  ({time.time() - t0:.3f}s)")
t1 = time.time()

ans2 = 0
for line in lines:
    ans2 += 1 if valid2(list(line.split())) else 0
print("part 2:", ans2, f"  ({time.time() - t1:.3f}s)")

from utils import load_lines

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


lines = load_lines(INPUT_FILE)

ans1 = 0
for line in lines:
    ans1 += 1 if valid(list(line.split())) else 0
print("part 1:", ans1)

ans2 = 0
for line in lines:
    ans2 += 1 if valid2(list(line.split())) else 0
print("part 2:", ans2)

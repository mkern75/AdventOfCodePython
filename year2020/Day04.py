from utils import load_text_blocks, is_int
import re

INPUT_FILE = "./year2020/data/day04.txt"


def load_passports(filename):
    passports = []
    for text_block in load_text_blocks(filename):
        passport = dict()
        for line in text_block:
            passport.update(item.split(":") for item in line.split(" "))
        passports += [passport]
    return passports


def to_int(s):
    return int(s) if is_int(s) else 0


def valid1(passport):
    return len(set(passport.keys()).intersection({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})) == 7


def valid2(passport):
    if not valid1(passport):
        return False
    for key, value in passport.items():
        if key == "byr" and not (1920 <= to_int(value) <= 2002):
            return False
        if key == "iyr" and not (2010 <= to_int(value) <= 2020):
            return False
        if key == "eyr" and not (2020 <= to_int(value) <= 2030):
            return False
        if key == "hgt":
            if not value[-2:] in ["cm", "in"]:
                return False
            elif value[-2:] == "cm" and not (150 <= to_int(value[:-2]) <= 193):
                return False
            elif value[-2:] == "in" and not (59 <= to_int(value[:-2]) <= 76):
                return False
        if key == "hcl" and not re.match(r"^#[0-9a-f]{6}$", value):
            return False
        if key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if key == "pid" and not re.match(r"^[0-9]{9}$", value):
            return False
    return True


ans1, ans2 = 0, 0
for i, passport in enumerate(load_passports(INPUT_FILE)):
    if valid1(passport):
        ans1 += 1
    if valid2(passport):
        if i == 50:
            print(passport)
        ans2 += 1
print("part 1:", ans1)
print("part 2:", ans2)

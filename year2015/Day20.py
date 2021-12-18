import math

file = open("./year2015/data/day20.txt", "r")
lines = [line.rstrip('\n') for line in file]


def number_of_presents(house, multiplier, stop_delivery=math.inf):
    c = 0
    for n in range(1, int(math.sqrt(house)) + 1):
        if house % n == 0:
            nn = house // n
            if nn <= stop_delivery:
                c += n
            if nn > n and n <= stop_delivery:
                c += nn
    return c * multiplier


def find_house(target_presents, multiplier, stop_delivery=math.inf):
    house = 1
    while number_of_presents(house, multiplier, stop_delivery) < target_presents:
        house += 1
    return house


target_presents = int(lines[0])
print(find_house(target_presents, 10))
print(find_house(target_presents, 11, 50))

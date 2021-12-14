from json import loads  # something learnt!

file = open("./year2015/data/day12.txt", "r")
lines = [line.rstrip('\n') for line in file]


def parse(item, ignore_red=False):
    if type(item) == int:
        return item
    elif type(item) == list:
        return sum([parse(sub_item, ignore_red) for sub_item in item])
    elif type(item) == dict and not (ignore_red and "red" in item.values()):
        return parse(list(item.keys()), ignore_red) + parse(list(item.values()), ignore_red)
    else:
        return 0


print(sum([parse(loads(line)) for line in lines]))
print(sum([parse(loads(line), True) for line in lines]))

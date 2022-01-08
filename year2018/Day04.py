from utils import load_lines
from collections import namedtuple, Counter
import re
from datetime import datetime

INPUT_FILE = "./year2018/data/day04.txt"
Event = namedtuple("event", "date_time info")

events = []
for line in load_lines(INPUT_FILE):
    m = re.compile(r"\[(.*)\] (.*)").match(line)
    events += [Event(datetime.strptime(m.group(1), "%Y-%m-%d %H:%M"), m.group(2))]
events = sorted(events, key=lambda event: event.date_time)

total, by_minute = Counter(), Counter()
for event in events:
    if event.info.startswith("Guard"):
        guard = int(event.info.split()[1][1:])
    elif event.info == "falls asleep":
        falls_asleep = event.date_time.minute
    elif event.info == "wakes up":
        wakes_up = event.date_time.minute
        total[guard] += wakes_up - falls_asleep
        for minute in range(falls_asleep, wakes_up):
            by_minute[(guard, minute)] += 1

guard_most_asleep = total.most_common()[0][0]
minute_most_asleep = 0
for minute in range(60):
    if by_minute[(guard_most_asleep, minute)] > by_minute[(guard_most_asleep, minute_most_asleep)]:
        minute_most_asleep = minute
print("part 1:", guard_most_asleep * minute_most_asleep)

guard_minute_most_asleep = by_minute.most_common()[0][0]
print("part 2:", guard_minute_most_asleep[0] * guard_minute_most_asleep[1])

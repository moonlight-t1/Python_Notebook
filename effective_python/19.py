## 리턴값 unpacking

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)

print(f"최대 길이: {longest:>4.0%}")
print(f"최소 길이: {shortest:>4.0%}")


## namedtuple
# 튜플인데 딕셔너리의 성격을 가지고 있다
from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", "x y")

pt1 = Point(1.0, 5.0)
pt2 = Point(2.0, 2.5)
# pt1 = Point(x=1.0, y=5.0)
# pt2 = Point(x=2.0, y=2.5)

length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
print(length)

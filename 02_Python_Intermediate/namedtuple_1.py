from collections import namedtuple
from math import sqrt

# general usage of tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

l_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt2[1]) ** 2)

print(l_leng1)


# use namedtuple
Point = namedtuple("Point", "x y")


# declare two points
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_leng2 = sqrt((pt4.x - pt3.x) ** 2 + (pt4.y - pt3.y) ** 2)

print(l_leng2)
print(l_leng1 == l_leng2)

print(pt3)
print(pt4)

print(pt3.x, pt3.y)
print(pt4[0], pt4[1])
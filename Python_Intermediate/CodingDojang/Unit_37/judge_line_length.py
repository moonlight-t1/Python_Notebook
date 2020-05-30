import math


class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(
    int, input().split()
)


def line(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


line1 = line(p[0].x, p[1].x, p[0].y, p[1].y)
line2 = line(p[1].x, p[2].x, p[1].y, p[2].y)
line3 = line(p[2].x, p[3].x, p[2].y, p[3].y)

# line1 = math.sqrt((p[0].x - p[1].x) ** 2 + (p[0].y - p[1].y) ** 2)
# line2 = math.sqrt((p[1].x - p[2].x) ** 2 + (p[1].y - p[2].y) ** 2)
# line3 = math.sqrt((p[2].x - p[3].x) ** 2 + (p[2].y - p[3].y) ** 2)
length = line1 + line2 + line3

print(length)


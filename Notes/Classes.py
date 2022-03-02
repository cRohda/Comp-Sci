from math import hypot


class Point:
    def __init__(self, x_coord = 0, y_coord = 0 ):
        self.x = x_coord
        self.y = y_coord


p1 = Point(3, 5)
p2 = Point(6, -1)
p3 = Point(10, 7)


def length(a, b):
    return hypot((b.x - a.x), (b.y - a.y))


perimeter = length(p1, p2) + length(p2, p3) + length(p3, p1)
print(perimeter)
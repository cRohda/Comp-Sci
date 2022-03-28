class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = yield

    def distance(self, np):
        dist = ((self.x - np.x)**2 + (self.y - np.y)**2)**0.5
        return dist


p1 = Point(5, 1)
p2 = Point(3, 4)

dist = p1.distance(p2)
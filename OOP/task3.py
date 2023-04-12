class Parallelogram:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
class Square(Parallelogram):
    def __init__(self, length):
        self.length = length
    def get_area(self):
        return self.length ** 2

parallel = Parallelogram(3,4)
print(parallel.get_area())
sq = Square(3)
print(sq.get_area())

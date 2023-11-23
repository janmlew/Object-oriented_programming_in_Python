class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self, w, w)
        self.w = w
        self.h = w

sq = Square(4)
sq.h = 7
rec = Rectangle(3, 5)
print(sq.h)
print(sq.w)

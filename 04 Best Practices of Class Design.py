class Rectangle:
    def __init__(self, w, h):
        self.h = h
        self.w = w

    def set_h(self, h):
        self.h = h

    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        super().__init__(w, w)
        self.w = w
        self.h = w

    def set_h(self, h):
        self.h = h
        self.w = h

    def set_w(self, h):
        self.h = h
        self.w = h


sq = Square(4)
sq.h = 7
rec = Rectangle(3, 5)
print(sq.h)
print(sq.w)

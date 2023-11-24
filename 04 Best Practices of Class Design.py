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


class BetterDate:
    _MAX_DAYS = 31
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    def _is_valid(self):
        if (self.day <= self._MAX_DAYS) and (self.month <= self._MAX_MONTHS):
            return True
        else:
            return False


bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())


class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError
        else:
            self._balance = new_bal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            raise ValueError
        else:
            self._balance = new_bal
        print("Setter method is called")


c = Customer('test', 1000)
c.balance = 2000
print(c.balance)

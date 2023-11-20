from datetime import datetime


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        # parts = datestr.split("-")
        # year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, datetime_object):
        year, month, day = datetime_object.year, datetime_object.month, datetime_object.day
        return cls(year, month, day)


# bd = BetterDate.from_str('2020-04-30')
today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)


class Employee:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    # pass
    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.bonus = None
        self.project = project

    def display(self):
        print("Manager", self.name)

    def give_raise(self, amount, bonus=1.05):
        Employee.give_raise(self, amount * bonus)


mng = Manager('Debbie Lashko', 86500)
print(mng.name)
mng.display()

mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)


class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            self.position = 10

    def draw(self):
        drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
        print(drawing)


class Racer(Player):
    MAX_SPEED = 5


r = Racer()
p = Player()
print(r.MAX_SPEED)
print(p.MAX_SPEED)

p.draw()
p.move(4)
p.draw()
p.move(5)
p.draw()
p.move(3)
p.draw()

p1, p2 = Player(), Player()
print("MAX_SPEED of p1 and p2 before assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
print(Player.MAX_SPEED)

p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
print(Player.MAX_SPEED)

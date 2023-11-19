from datetime import datetime
import math


class MyCounter:
    def __init__(self):
        self.count = None

    def set_count(self, n):
        self.count = n


mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
        self.hire_date = datetime.today()

    # def set_name(self, new_name: str):
    # assert isinstance(new_name, str)
    # self.name = new_name

    # def set_salary(self, new_salary: int):
    # assert isinstance(new_salary, int)
    # self.salary = new_salary

    def give_raise(self, raise_amount: int):
        assert isinstance(raise_amount, int)
        self.salary = self.salary + raise_amount

    @property
    def monthly_salary(self) -> float:
        return self.salary / 12


emp = Employee("Tav", -1000)
# emp.set_name('Korel Rossi')
# emp.set_salary(50000)

print(emp.name)
print(dir(emp))
print(emp.salary)

emp.salary = emp.salary + 1500

print(emp.salary)

emp.give_raise(166)

print(emp.salary)
print(emp.monthly_salary)


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def reflect(self, axis):
        if axis == 'x':
            self.x = self.x
            self.y = -self.y
        elif axis == 'y':
            self.x = -self.x
            self.y = self.y
        else:
            print('axis should be either ''x'' or ''y''')
            self.x = self.x
            self.y = self.y


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

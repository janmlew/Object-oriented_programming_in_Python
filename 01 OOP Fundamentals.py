from datetime import datetime

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

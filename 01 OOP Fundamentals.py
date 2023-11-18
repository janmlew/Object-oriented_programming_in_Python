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
    def __init__(self):
        self.salary = None
        self.name = None

    def set_name(self, new_name: str):
        assert isinstance(new_name, str)
        self.name = new_name
        
    def set_salary(self, new_salary: int):
        assert isinstance(new_salary, int)
        self.salary = new_salary

    def give_raise(self, raise_amount: int):
        assert isinstance(raise_amount, int)
        self.salary = self.salary + raise_amount

    @property
    def monthly_salary(self) -> float:
        return self.salary / 12


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.name)
print(dir(emp))
print(emp.salary)

emp.salary = emp.salary + 1500

print(emp.salary)

emp.give_raise(166)

print(emp.salary)
print(emp.monthly_salary)

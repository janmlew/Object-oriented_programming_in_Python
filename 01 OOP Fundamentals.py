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
        self.name = None

    def set_name(self, new_name: str):
        assert isinstance(new_name, str)
        self.name = new_name


emp = Employee()

emp.set_name('Korel Rossi')

print(emp.name)

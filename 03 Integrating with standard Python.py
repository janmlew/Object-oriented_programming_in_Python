class BankAccount:
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        # return (self.number == other.number) and (type(self) == type(other))
        return (self.number == other.number) and (isinstance(self, BankAccount) == isinstance(other, BankAccount))


class Phone:
    def __init__(self, number=0):
        self.number = number


acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)

my_num = 5
my_str = "Hello"

f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)
print(f)
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
print(f)
f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)
print(f)


class Employee:
    salary: int
    name: str

    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        cust_str = """
        Employee name: {name}
        Employee salary: {salary}""".format(name=self.name, salary=self.salary)
        return cust_str

    def __repr__(self):
        return "Employee(\"{}\", {})".format(self.name, self.salary)


emp1 = Employee("Amar Howard", 30000)
print(emp1)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
print(repr(emp2))


def invert_at_index(x, ind):
    try:
        return 1 / x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")


a = [5, 6, 0, 7]

print(invert_at_index(a, 1))
print(invert_at_index(a, 2))
print(invert_at_index(a, 5))


class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if Employee.MIN_SALARY > salary:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")
        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")
        else:
            self.salary += amount

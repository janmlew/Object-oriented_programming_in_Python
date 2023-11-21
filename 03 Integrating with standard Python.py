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

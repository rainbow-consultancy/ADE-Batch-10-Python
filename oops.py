# Python - Object Oriented Programming Concepts
# (Encapsulation, Inheritance, Polymorphism, Abstraction)


# -- Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient balance")

# account = BankAccount(10000)
# account.deposit(5000)
# account.withdraw(3000)

# print(account.balance)


# Public, Protected and Private

class Employee:
    def __init__(self):
        self.name = "Lokesh" # public variable
        self._salary = 50000  # protected variable
        self.__bonus = 20000 # private variable


# lokesh = Employee()
# print(lokesh.name)
# print(lokesh._salary)
# print(lokesh.__bonus)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("insufficient balance")
    
    def __display_balance(self):
        return self.__balance
    
    def get_balance(self):
        return self.__display_balance()

account = BankAccount(10000)
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())
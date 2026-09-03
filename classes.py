# Python Classes

# attributes - These are the characteristics, variables 
# methods/functions - actions


# syntax
# class BakeryBiscuit:
    
#     name = "KarachiBiscuit"
#     def choco_biscuit(self):
#         print("Add choco chips and bake the biscuits")

# biscuit = BakeryBiscuit()
# biscuit.choco_biscuit()

# cookie = BakeryBiscuit()
# cookie.choco_biscuit()

class Dog:
    
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        print("Init method is called")
        
    def bark(self):
        print(f"{self.name} is barking and it's breed is {self.breed}")


# tommy = Dog("Tommy", "AfricanHound")
# tommy.bark()

# jimmy = Dog("Jimmy", "DoberMan")
# jimmy.bark()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(self.name, self.salary)
        
emp1 = Employee("Harish", 40000)
emp2 = Employee("Lokesh", 50000)

# emp1.display()
# emp2.display()

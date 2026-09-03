# inheritance

# Parent Class / Base Class
# Child Class / Derived Class

class ParentClass():
    
    Surname = "SomeSurname"
    def hsr_property(self):
        print("Own a 2bhk")

    def electronic_city(self):
        print("Owns a villa")
        
class ChildClass(ParentClass):
    def btm_property(self):
        print("Owns a commericial complex")


# cc = ChildClass()
# print(cc.Surname)
# cc.hsr_property()
# cc.electronic_city()
# cc.btm_property()


# multiple inheritance
class FatherClass():
    
    Surname = "SomeSurname"
    def hsr_property(self):
        print("Own a 2bhk")

    def electronic_city(self):
        print("Owns a villa")
        

class MotherClass():
    
    def sarjapur_property(self):
        print("Own a Mansion")
        
    
class ChildClass(FatherClass, MotherClass):
    pass

# cc = ChildClass()
# cc.sarjapur_property()
# cc.electronic_city()


# multi-level inheritance

class GrandParent():
    def hsr_property(self):
            print("Own a 2bhk")
    
    def electronic_city(self):
        print("Owns a villa")
        
class FatherClass(GrandParent):
    def sarjapur_property(self):
        print("Own a Mansion") 

class ChildClass(FatherClass):
    pass

# cc = ChildClass()
# cc.hsr_property()
# cc.sarjapur_property()


class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child class")


# c = Child()
# c.show()


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

emp = Employee("Kalyan", 40000)
print(emp.name)
print(emp.salary)

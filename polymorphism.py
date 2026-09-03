# OOPS - Polymorphism (one thing having many forms)

class Cat:
    def sound(self):
        print("Cat Sound")
        
class Dog:
    def sound(self):
        print("Dog Sound")  
        

dog = Dog()
cat = Cat()

# dog.sound()
# cat.sound()


class Circle:
    def area(self, r):
        print(f"Area of the circle - {3.14 * r**2}")

class Rectangle:
    def area(self, l, w):
        print(f"Area of the Rectangle - {l*w}")
        
c = Circle()
r = Rectangle()

# c.area(10)
# r.area(30, 40)

# method overiding 
# method overloading (is not supported in python)

def add(a, b, c=0):
    return a+b+c

def add(*args):
    return sum(args)

print(add(10, 20, 30, 40))
print(add(10, 20))


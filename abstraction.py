# OOPS - Abstraction

from abc import ABC, abstractmethod


# Abstract Base Class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    
    def sound(self):
        print("Dog is barking")
    
    def feed_dog(self):
        print("Dog is getting food")


dog = Dog()
dog.feed_dog()
dog.sound()

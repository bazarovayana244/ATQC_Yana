###Create an abstract class A with a few abstract methods.###
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def move(self):
        pass

###Create a child class B of A and don't implement abstract methods. Try to create an instance of class B.###
class Cat(Animal):
    pass
try:
    cat = Cat()
except TypeError as e:
    print(e)

###Create a child class B of A and implement these methods. Create an instance of class B. Call B class methods.###
class Cat(Animal):
    def speak(self):
        return "Meow"
    def move(self):
        return "Walk"
cat = Cat()
print(cat.speak())
print(cat.move())

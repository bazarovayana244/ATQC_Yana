###Create classes A, B and C that will have the same method name, but different implementations.###
class Cat:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"The cat`s name is {self.name}"
class Dog:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"The dog`s name is {self.name}"
class Bird:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"The bird`s name is {self.name}"

###Create an interface that will interact (call) with this method. E.g. function that accepts a class instance.###

def show_info(animal):
    print(animal.info())

###Create instances of classes A, B and C. Pass them into the interface.###
cat = Cat("Luna")
dog = Dog("Miley")
bird = Bird("Tweety")

show_info(cat)
show_info(dog)
show_info(bird)

###Create a class with a few class attributes. Add constructor with a few arguments and instance attributes.###

class Cat:
    species = "Felis silvestris"
    tail = True
    sound = "Meow"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

###Create a special method of a class Cat that will return a string representation of a few instance attributes.###
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"Cat(self.name, self.color, self.age)"

cat1 = ("Luna", "black", 5)
cat2 = ("Ruby", "ginger", 1)
print(cat1)
print(cat2)

###Add a few methods to the class that would interact with class attributes.###
class Cat:
    species = "Felis silvestris"
    tail = True
    sound = "Meow"

    @classmethod
    def get_species(cls):
        return f"All cats belong to {cls.species}"
    @classmethod
    def get_sound(cls, new_sound):
        cls.sound = new_sound
        return f"All cats say {new_sound}"

print(Cat.get_species())
print(Cat.get_sound("Nyav"))

###Add a few methods to the class that would interact with instance attributes.###
class Cat:
    species = "Felis silvestris"
    tail = True
    sound = "Meow"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def info(self):
        return f"{self.name}, {self.color}, {self.age}"

    def new_age(self):
        self.age += 1
        return f"{self.name} is now {self.age}"

cat1 = Cat("Luna", "black", 5)
cat2 = Cat("Ruby", "ginger", 1)
print(cat1.info())
print(cat2.new_age())

###Create an instance of a class and pass a few arguments.###
class Cat:
    species = "Felis silvestris"
    tail = True
    sound = "Meow"

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def info(self):
        return f"{self.name}, {self.color}, {self.age}"
cat1 = Cat("Luna", "black", 5)
cat2 = Cat("Ruby", "ginger", 1)
print(cat1.info())

###Using an instance of a class, call its methods and pass some arguments if applicable.###
class Cat:

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        return f"{self.name} says Meow"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}."

    def rename(self, new_name):
        self.name = new_name
        return f"Rename to {self.name}"

cat1 = Cat("Luna", "black", 5)
print(cat1.meow())
print(cat1.birthday())
print(cat1.rename("Ruby"))
print(cat1.meow())

###Using an instance of a class, change the value of attributes.###
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def info(self):
        return f"{self.name} is a {self.color} cat, {self.age} years old"
cat1 = Cat("Luna", "black", 5)
print(cat1.info())
cat1.color = "white"
cat1.age = 6
print(cat1.info())

###Using an instance of a class, add a new attribute.###
class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def info(self):
        return f"{self.name} is a {self.color} cat, {self.age} years old"
cat1 = Cat("Luna", "black", 5)
print(cat1.info())
cat1.owner = "John"
print(f"{cat1.owner} is the owner of {cat1.name}")

###Create class A (add attributes, constructor and methods). Create class B that will inherit class A.
# Add a few new methods in class B and override at least one method from class A in class B.###
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

class HouseCat(Cat):
    def __init__(self, name, color, age, owner):
        super().__init__(name, color, age) #call parent constructor
        self.owner = owner
    def info(self): #override info method
        return f"{self.name}, {self.color}, {self.age}, {self.owner}"

    def change_owner(self, new_owner): #add new method
        self.owner = new_owner
        return f"{self.name} has a new owner {self.owner}"

    def make_sound(self): #add new method
        return f"{self.name} says {self.sound}"

###Create an instance of class B and call a few of its methods (new, overridden and only implemented in class A).###
cat2 = HouseCat("Ruby", "Ginger", 1, "John")
print(cat2.info()) #overriden method
print(cat2.change_owner("Bob")) #new method
print(cat2.make_sound()) #new method
print(cat2.new_age()) #only implemented in class A

###Create classes A and B (add attributes, constructor and methods. Add methods that have the same name in both classes).
# Create class C that will inherit both A and B classes.###
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

class Dog:
    species = "Canis lupus"
    sound = "Bark"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def info(self):
        return f"{self.name}, {self.breed}, {self.age}"

    def new_age(self):
        self.age += 1
        return f"{self.name} is now {self.age}"

class Pet(Cat, Dog):
    def __init__(self, cat_name, cat_color, cat_age, dog_name, dog_breed, dog_age):
        Cat.__init__(self, cat_name, cat_color, cat_age)
        Dog.__init__(self, dog_name, dog_breed, dog_age)
        self.cat_name = cat_name
        self.dog_name = dog_name
        self.cat_age = cat_age
        self.dog_age = dog_age

###Create an instance of class C. Call its methods and attributes. Call the method that was implemented in both A and B
# classes (that have the same name) and verify what method is called (implemented in A or B).###

my_pet = Pet("Luna", "black", 5, "Jack", "beagle", 2)

#Call attributes
print(my_pet.cat_name) #class Cat attribute
print(my_pet.dog_name) #class Dog attribute
print(my_pet.color) #class Cat attribute
print(my_pet.breed) #class Dog attribute
print(my_pet.cat_age) #class Cat attribute
print(my_pet.dog_age) #class Dog attribute
print(my_pet.age) #class Dog age +1, because of calling this method print(my_pet.new_age())

#Call methods
print(my_pet.info()) #Class Dog for name and age because of reassignment and class Cat for color
print(my_pet.new_age()) #Class Dog because of reassignment

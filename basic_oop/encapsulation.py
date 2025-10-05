###Create class A. Add a few private/protected attributes and private/protected methods.###
class Cat:
    def __init__(self, name, color, age):
        self._name = name #protected attribute
        self.__color = color #private attribute
        self.age = age #public attribute

    def info(self): #public method
        return f"Name: {self._name}, Color: {self.__color}, Age: {self.age}"

    def _make_sound(self): #protected method (can be used in subclasses)
        return "Meow"

    def __change_color(self, new_color):
        self.__color = new_color
        return f"{self._name} color has been changed to {self.__color}"

###Create an instance of class A. Verify that private methods and attributes can't be called directly.
# Verify whether protected attributes and methods can be called outside of class A.###

cat1 = Cat("Luna", "black", 5)

print(cat1.info()) #public method can be called
print(cat1.age) #public attribute can be called

print(cat1._name) #protected attribute can be called but is a warning
print(cat1._make_sound()) #protected method can be called but is a warning

try:
    print(cat1.__color) #private attribute - no access
except AttributeError:
    print("Access denied. Private attribute '__color'")

try:
    print(cat1.__change_color("orange")) #private method - no access
except AttributeError:
    print("Access denied. Private method '__change_color'")

###Find a way to call and change private attributes and methods outside of class A respectively.###
#Using name mangling
print(cat1._Cat__color)
print(cat1._Cat__change_color("orange"))

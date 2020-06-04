''' Explaining inheritance example1 '''
from parent import Animal


# Defining Subclass - inherits all attributes of Animal class
class Cat(Animal):
    def speak(self):  # added new functionality
        return "meow"

    def __str__(self):  # overrides existing __str__ functionality
        return ("cat:" + str(self.name) + ":" + str(self.age))


# validating inheritance properties
a = Animal(2)
c = Cat(3)
print(c.get_age())
print(c.get_name())
print(c.speak())
# print(a.speak())  # gives error
print(c)
print(a)

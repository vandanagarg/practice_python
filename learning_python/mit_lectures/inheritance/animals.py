''' Explaining different concepts related to information hiding/
encapsulation (using getter and setters), using default arguments,
inheritance and class/instance variables '''


# defining a class
class Animal(object):
    def __init__(self, age):
        # self.age = age  # if attribute is changed to years
        self.years = age
        self.name = None

    # creating getter methods
    def get_age(self):
        # return self.age  # updated to years attribute
        return self.years

    def get_name(self):
        return self.name

    # creating setter methods
    def set_age(self, newage):
        self.age = newage  # if not changed, creates a new attribute age
        self.years = newage  # updates new/existing attribute years

    def set_name(self, newname=""):
        self.name = newname

    # special method __str__
    def __str__(self):
        return "animal:", str(self.name), ":", str(self.age)


# creating instance
myanimal = Animal(4)
# print(myanimal.age)  # gives error since no such attribute age

a = Animal(3)
# print(a.age)  # allowed, but not recommended
# also, gives error since no such attribute age
# Ways to information hiding
print(a.get_age())  # recommended way

# passing a new age
a.set_age(7)
print(a.get_age())  # updates years attribute
print(a.age)  # creates a new age attribute; hence no error

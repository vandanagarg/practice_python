''' Explaining inheritance example2 '''
from parent import Animal


# Defining Subclass - inherits all attributes of Animal class
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)  # calls Animal constructor
        self.set_name(name)  # calls Animal's method
        self.friends = []  # new data attribute

    # creating new methods
    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        return "hello"

    def age_diff(self, other):
        diff = self.age - other.age
        return (abs(diff), "year difference")

    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)


# validating new methods in subclass
p1 = Person("jack", 30)
p2 = Person("jill", 25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
print(p1.speak())
print(p1.age_diff(p2))

# adding friends
p1.add_friend("luke")
p1.add_friend("sam")
p1.add_friend("luke")
print(p1.get_friends())
print(p2.get_friends())

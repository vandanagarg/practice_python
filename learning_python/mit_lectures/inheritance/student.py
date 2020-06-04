''' Explaining inheritance example3 using Person as Parent class
and building layers of abstraction in subclass '''
import random
from person import Person


# Defining Subclass - inherits all attributes of Person and Animal class
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()  # random() gives back a float in [0, 1)
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("I am watching TV")

    def __str__(self):
        return ("student:" + str(self.name) + ":" +
                str(self.age) + ":" + str(self.major))


print("\n student tests")
s1 = Student("alice", 20, "CS")
s2 = Student("beth", 18)
print(s1)
print(s2)
print(s1.get_name(), "says:", end=" ")
s1.speak()
print(s2.get_name(), "says:", end=" ")
s2.speak()

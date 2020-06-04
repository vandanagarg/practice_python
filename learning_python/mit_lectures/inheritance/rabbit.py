''' Explaining class/instance variables '''
from parent import Animal


# Defining Subclass - inherits all attributes of Animal class
class Rabbit(Animal):
    # tag class variable value is shared between all instances of the class
    tag = 1  # gives unique id to each new rabbit instance

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        # instance variables values ex: parent1, parent2, rid
        # are limited to the particular instance
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    # getter methods specific for Rabbit class
    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    # special operator specific for Rabbit class
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)

    # to check equality: two rabbits are equal if they have same two parents
    def __eq__(self, other):
        # comparing id's of parents since they are unique
        # and we can't compare objects directly
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
            and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

    def __str__(self):
        return "rabbit:" + self.get_rid()


# validating values of class variable
r1 = Rabbit(4)
print(r1.get_rid())
r2 = Rabbit(5)
print(r2.get_rid())
print(Rabbit.tag)
r3 = Rabbit(2)
print(r3.get_rid())
print(Rabbit.tag)

# validating + operator between two rabbit instances
r4 = r1 + r2  # r1.__add__(r2)
# r4 is a new Rabbit instance with age 0, r4 got self(r1) as one parent and
# other(r2) as the other parent
print(r4)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

# validating rabbits equality
r5 = r3 + r4
r6 = r4 + r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5.__eq__(r6))
print("r4 and r6 have same parents?", r4.__eq__(r6))

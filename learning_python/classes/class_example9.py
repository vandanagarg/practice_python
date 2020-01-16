
class Circle():

    # Class Object Attribute
    PI = 3.14

    def __init__(self, radius= 1):
        self.radius = radius
        self.area = radius*radius*self.PI  # self.pi can also be written as Circle.pi

    #Method

    def get_circumference(self):
        return self.radius * self.PI * 2

my_circle = Circle(30)

print(my_circle.PI)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)

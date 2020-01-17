class Cylinder:

    def __init__(self, radius= 1, height = 1):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.height * 3.14 * (self.radius**2)

    def surface_area(self):
        circle_area = 3.14 * (self.radius**2)
        return (2* circle_area) + (2* 3.14 * self.radius * self.height)

cyl1 = Cylinder(3,2)
print(cyl1.volume())
print(cyl1.surface_area())


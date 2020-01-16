class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) **  0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

c = Coordinate(3,4)
print(c)
# <__main__.Coordinate object at 0x000000000238ABC8>  o/p without __str__ method

zero = Coordinate(0,0)
print(c.distance(zero))

#or
print(Coordinate.distance(c,zero))

# to check if an object is a Coordinate
print(isinstance(c,Coordinate))  # True as c is an object of type Coordinate




''' Creating a Class/ random abstract datatype of type Coordinate
This is an example for OOPS concept in programming '''


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        ''' Python calls __str__ method when used with
        print on the class object. Here we define that a
        Coordinate object on print must return below string '''
        return "<" + str(self.x) + "," + str(self.y) + ">"


c = Coordinate(3, 4)
# representation of an object
print(c)
# <__main__.Coordinate object at 0x000000000238ABC8> o/p without __str__ method

# also it makes sense that Coordinate itself is a class and its datatype is
# type as datatype of any other datastructure is just type
print(Coordinate)  # <class '__main__.Coordinate'>
print(type(Coordinate))  # <class 'type'>
print(type(int))  # <class 'type'>
print(type(list))  # <class 'type'>
print(type(str))  # <class 'type'>
print(type("int"))  # <class 'str'>

zero = Coordinate(0, 0)
print(zero)
print(c.distance(zero))

# or
print(Coordinate.distance(c, zero))

# to check if an object is a Coordinate
print(isinstance(c, Coordinate))  # True as c is an object of type Coordinate

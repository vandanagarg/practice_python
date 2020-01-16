# class Coordinate(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self,other):
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq + y_diff_sq) **  0.5
#     def __str__(self):
#         return "<" + str(self.x) + "," + str(self.y) + ">"
#
# c = Coordinate(3,4)
# print(c)
# # <__main__.Coordinate object at 0x000000000238ABC8>  o/p without __str__ method
#
# zero = Coordinate(0,0)
# print(c.distance(zero))
#
# #or
# print(Coordinate.distance(c,zero))
#
# # to check if an object is a Coordinate
# print(isinstance(c,Coordinate))  # True as c is an object of type Coordinate
#
#


class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num nd denom are integers"""
        assert type(num) == int and type(denom)== int
        self.num =  num
        self.denom = denom
    def __str__(self):
        """Returns  a string representation of self"""
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """Returns a new fraction representing the addition"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction  """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)


    def __float__(self):
        """Returns a float value of the fraction"""
        return self.num/self.denom

    def inverse(self):
        """Returns a new fraction representing """
        return Fraction(self.denom, self.num)


a = Fraction(1,4)
b = Fraction(3,4)
c = a + b #c is fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

##c = Fraction(3.14, 2.7)  # assertion error
## print a*b #error, did not define how to multiply



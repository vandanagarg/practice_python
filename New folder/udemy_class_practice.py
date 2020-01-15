# class Line:
#
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return (((x2-x1)**2) + ((y2- y1)**2) ) **  0.5
#
#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (y2 - y1)/(x2- x1)
#
# coordinate1 = (3,2)
# coordinate2 = (8,10)
# l1 = Line(coordinate1, coordinate2)
#
# print(l1.distance())
# print(l1.slope())


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
# c1 = Coordinate(3,2)
# # print(c1)
# # <__main__.Coordinate object at 0x000000000238ABC8>  o/p without __str__ method
#
# c2 = Coordinate(8,10)
# print(c1.distance(c2))
#9.433981132056603
#or
# print(Coordinate.distance(c1,c2))
#
# # to check if an object is a Coordinate
# print(isinstance(c,Coordinate))  # True as c is an object of type Coordinate
#
#


# class Fraction(object):
#     """
#     A number represented as a fraction
#     """
#     def __init__(self, num, denom):
#         """ num nd denom are integers"""
#         assert type(num) == int and type(denom)== int
#         self.num =  num
#         self.denom = denom
#     def __str__(self):
#         """Returns  a string representation of self"""
#         return str(self.num) + "/" + str(self.denom)
#     def __add__(self, other):
#         """Returns a new fraction representing the addition"""
#         top = self.num*other.denom + self.denom*other.num
#         bott = self.denom*other.denom
#         return Fraction(top, bott)
#
#     def __sub__(self, other):
#         """ Returns a new fraction representing the subtraction  """
#         top = self.num*other.denom - self.denom*other.num
#         bott = self.denom*other.denom
#         return Fraction(top, bott)
#
#
#     def __float__(self):
#         """Returns a float value of the fraction"""
#         return self.num/self.denom
#
#     def inverse(self):
#         """Returns a new fraction representing """
#         return Fraction(self.denom, self.num)
#
#
# a = Fraction(1,4)
# b = Fraction(3,4)
# c = a + b #c is fraction object
# print(c)
# print(float(c))
# print(Fraction.__float__(b))
# print(float(b.inverse()))
# print(Fraction.__float__(Fraction.inverse(b)))
#
# ##c = Fraction(3.14, 2.7)  # assertion error
# ## print a*b #error, did not define how to multiply
#
#

# class Cylinder():
#
#     def __init__(self, radius= 1, height = 1):
#         self.radius = radius
#         self.height = height
#
#     def volume(self):
#         return self.height * 3.14 * (self.radius**2)
#
#     def surface_area(self):
#         circle_area = 3.14 * (self.radius**2)
#         return (2* circle_area) + (2* 3.14 * self.radius * self.height)
#
# cyl1 = Cylinder(3,2)
# print(cyl1.volume())
# print(cyl1.surface_area())


#make bank account
#deposit
#withdraw- shouldn't exceed balance
#print balances, individual data
#
# class Bank():
#
#     def __init__(self,name, bank_balance=  0):
#         self.name = name
#         assert type(bank_balance) == int
#         self.bank_balance = bank_balance
#
#         # print("Account holder name: {}".format(self.name))
#         # print("Account Balance: ${}".format(self.bank_balance))
#         print("Your current bank balance is ${}".format(self.bank_balance))
#
#
#     def deposits(self, deposit_amount):
#         assert type(deposit_amount) == int
#         self.bank_balance = self.bank_balance + deposit_amount
#         print("Account updated with ${}".format(deposit_amount))
#         print("Updated bank balance is ${}".format(self.bank_balance))
#
#     def withdraw(self,withdraw_amount):
#         assert type(withdraw_amount) == int
#         if self.bank_balance >= withdraw_amount:
#             self.bank_balance = self.bank_balance - withdraw_amount
#             print("Account updated with ${}".format(withdraw_amount))
#             print("Updated bank balance is ${}".format(self.bank_balance))
#         else:
#             print("Your account balance is low. Please enter a value less than ${}".format(self.bank_balance))
#             exit
#
#     def __str__(self):
#         return ("Account holder name: {} \nAccount Balance: ${}".format(self.name, self.bank_balance))
#
#
# bank = Bank("Vandana", 1000)
# # print(bank.name)
# # print(bank.bank_balance)
# # print(Bank)
# print(bank)
# # print(bank.deposits(2000))
# # bank.deposits(2000)
# take_money = bank.withdraw(500)
# take_money = bank.withdraw(500)
# # print(take_money)

# from inheritance import myfunc
# myfunc()
#
#
# from mypackage.main_program import mainprogram
# from mypackage.sub_package import sub_program
#
# mainprogram()
#
# sub_program.subprogram()



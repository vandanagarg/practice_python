# printing numbers and basic arithmetic operations using numbers
print(2)
print(1-2.656)
print(3 * (4 +5))
print(10 % 3)

# printing a number as a string (typecasting)
my_num = 3
print(str(my_num) + " my fav number")  # so in order to print a number along with a string we must convert a number too in string format else it gives error

#some basic functions for numbers:
my_num = -5
print(abs(my_num))
print(pow(3.2, 2))  #3.2^2
print(max(3.2, 2))  
print(min(3.2, 2))  
print(round(56.8))

#some advanced functions using library

from math import *
print(floor(56.8))
print(ceil(56.8))
print(sqrt(25))


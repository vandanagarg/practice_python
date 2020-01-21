#problem 2

try:
    x= 5
    y= 0
    z= x/y
except ZeroDivisionError:
    print("Oh dear division by zero is not allowed as per maths :) try again!!")
except :
    print("Something went wrong.")
finally:
    print("All done.")

# Try Except block

try:
    number = int(input("Enter a number : "))
    print(number)
except:  # here this is a very broad exception as it will throw a general exceptions for all the errors that come in try statements
    # so we should try to generalize this
    print("invalid input !!")

'''so now this try and except block is a small one and is just limited to one case , but what happens when we have different line of codes
and they give different kind of errors , so in that case in order to throw exceptions with respect to the kind of error we are getting
we must use separate exception blocks to handle them per the errors generated in the case the o/p throws error.
'''

try:
    value = 10/0
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError:
    print("Divide by Zero!!")
except ValueError:
    print("invalid input !!")

# if you want to store error exception as a variable and then want to print that out we can use it as below:

try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)
    
   
#    o/p
#
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# Enter a number : jhg
# invalid input !!
# Divide by Zero!!
# division by zero
#
# Process finished with exit code 0

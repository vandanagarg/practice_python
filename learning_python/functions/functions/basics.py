#functions - collection of code to perform a task..we need to use "def" in python in order to start a function
# any code inside the function needs to be indented #name all should be in lowercase and use _ if needed for more words.

def sayhi():
    print("Hello User")

sayhi() # calling function

#passing parameters #can give any n number of parameters
def sayhi(name):
    print("Hello "+ name)

sayhi("Mike") # calling function by passing parameter

#return statement # basically used when we want some output to be returned via a function/caller, instead of an explicit print statement
#return always breaks the flow of a function so if we put any line of code after return statement , it will be overlooked and will never execute.
def cube(num):
    return num*num*num  #if we dont put return in front of this then if we try to print o/p it returns nothing (either blank or NONE as o/p)
    print("code")  #this line of code will never be executed

print("result1: "+ str(cube(3)))

result = cube(3)
print("result2: "+ str(result))


##this line of code give no o/p
def cube_num(num):
    num*num*num
    
cube_num(5)

##this line of code give  o/p as NONE
def cube_none(num):
    num*num*num
    
print("result4: "+ str(cube_none(4)))

##this line of code give  o/p as 27
def cube_return(num):
    return num*num*num
    
print("result5: "+ str(cube_return(3)))

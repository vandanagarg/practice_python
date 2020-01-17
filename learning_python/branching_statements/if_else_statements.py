#if statements
#using if statement(special structure) that can help code to take decisions #to execute certain code if certain conditions are true else others

is_male = True

if is_male:  #this is assummed to be a true condition
    print("You are a male")  #o/p You are a male
else:
    print("You are not a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")  #o/p You are not a male

# with 2 variables
is_male= False
is_tall= True

#2ways: 1. with OR operator 2. with AND operator

if is_male or is_tall:
    print("You are a male or tall or both")  #o/p You are a male or tall or both
else:
    print("You are neither male nor tall")


##2nd condition
is_male= False
is_tall= False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")  #o/p You are neither male nor tall

#2. AND operator

is_male= False
is_tall= True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or not tall")  #o/p You are either not a male or not tall

##another condition with NOT
is_male= True
is_tall= False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):  #else if
    print("You are a short male")  #o/p You are a short male
else:
    print("You are either not a male or not tall")

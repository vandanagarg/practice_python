#decorator that allows to add on extra functionality to an already existing function
#use @ operator and is placed on the top of the original function.

def func():
    return 1

print(func())

#functions are objects that can be passed into another objects
def hello():
    return "Hi !!"


print(hello())
print(hello)
greet = hello()
print(greet)
greets = hello
print(greets)

def hello(name = "jose"):
    print("The hello() function has been executed! ")

    def greet():
        return  "\t This is greet() func inside hello() !"

    def welcome():
        return  "\t This is welcome() func inside hello() !"

    print(greet())
    print(welcome())
    print("End of the func hello()")

hello()


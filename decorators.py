#decorator that allows to add on extra functionality to an already existing function
#use @ operator and is placed on the top of the original function.

# def func():
#     return 1
#
# print(func())

#functions are objects that can be passed into another objects
# def hello():
#     return "Hi !!"
#
#
# print(hello())
# print(hello)
# greet = hello()
# print(greet)
# greets = hello
# print(greets)

# def hello(name = "jose"):
#     print("The hello() function has been executed! ")
#
#     def greet():
#         return  "\t This is greet() func inside hello() !"
#
#     def welcome():
#         return  "\t This is welcome() func inside hello() !"
#
#     print(greet())
#     print(welcome())
#     print("End of the func hello()")
#
# hello()


# def hello(name = "jose"):
#     print("The hello() function has been executed! ")
#
#     def greet():
#         return  "\t This is greet() func inside hello() !"
#
#     def welcome():
#         return  "\t This is welcome() func inside hello() !"
#
#     print("End of the func hello() and will now return function")
#
#     if name == "jose":
#         return greet
#     else:
#         return welcome
#
# my_new_func = hello()
# print(my_new_func)
# print(my_new_func())



# def hello():
#     return "VAndana"
#
# def other(some_func):
#     print("Other code here")
#     print(some_func)
#
# other(hello())


def new_decorator(original_func):

    def wrap_func():  # func that needs to be added in original func
        print("Some extra code, before the original func")

        original_func()

        print("Some extra code , after original func")

    return wrap_func

# def func_needs_decorator():
#     print("I want to be decorated.")

# func_needs_decorator()

# decorated_func =  new_decorator(func_needs_decorator)
# decorated_func

#OR

@new_decorator
def func_needs_decorator():
    print("I want to be decorated.")

func_needs_decorator()
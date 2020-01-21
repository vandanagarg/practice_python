# decorator example2

def hello(name = "jose"):
    print("The hello() function has been executed! ")

    def greet():
        return  "\t This is greet() func inside hello() !"

    def welcome():
        return  "\t This is welcome() func inside hello() !"

    print("End of the func hello() and will now return function")

    if name == "jose":
        return greet
    else:
        return welcome

my_new_func = hello()
print(my_new_func)
print(my_new_func())


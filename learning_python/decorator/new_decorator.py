#decorator example3

def hello():
    return "VAndana"

def other(some_func):
    print("Other code here")
    print(some_func)

other(hello())


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
''' shows how to to process different arguments inside functions,
also how to pass functions as arguments to other functions '''


def func_a():
    print("inside func a")


def func_b(y):
    print("inside func b")
    return y


def func_c(z):
    print("inside func c")
    return z()


print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

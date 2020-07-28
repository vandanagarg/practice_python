''' Reverse Arguments:
Given an arbitrary function, return a new function, which when called,
returns the result of the original function called with the arguments
in reversed order.
For example, if the original function, f, Is a pow function, f(2,3) = 8,
then the correct result is a function g, with g(3,2) - 9.
'''


def reversed_args(f):
    def new_func(*args):
        return f(*args[::-1])
    return new_func


# 2nd way:
def f(a, b):
    return a**b


def transform(f):
    return lambda *args: f(*args[::-1])


g = transform(f)

print(g(4, 5))  # g(5, 4)


print(pow(2, 3, 6))
print(pow(6, 3, 2))
new_func1 = reversed_args(pow)
print(new_func1(2, 3, 6))  # print(pow(6, 3, 2))
new_func2 = reversed_args(pow)
print(new_func2(6, 3, 2))  # print(pow(2, 3, 6))


def divide(a, b):
    return a / b


new_divide = reversed_args(divide)
print(new_divide(30.0, 10.0))
print(new_divide(10.0, 30.0))

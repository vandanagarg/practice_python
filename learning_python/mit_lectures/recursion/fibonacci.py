''' fibonacci series
In this cas we have more than 1 base case '''


def fib(x):
    ''' assume x an int>=0
    returns Fibonacci of x '''
    if x == 0 or x == 1:  # base cases
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

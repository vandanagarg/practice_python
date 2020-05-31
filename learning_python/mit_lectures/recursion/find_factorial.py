''' find out factorial using iteration and recursion '''


def factorial_iter(n):  # iteration
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


print(factorial_iter(5))


def factorial(n):  # recursion
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(4))

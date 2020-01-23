#Problem 15
#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0,
# is defined as being 1. Solve this using both loops and recursion.

#using loop


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


print(factorial(4))

#using recursion


def factorial_recursion(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)


print(factorial_recursion(4))


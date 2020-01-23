#Problem 2
#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fib(num):
    a = 0
    b = 1
    for n in range(num):
        yield a
        a, b = b, a+b


print(list(fib(10)))

for x in fib(10):
    print(x)

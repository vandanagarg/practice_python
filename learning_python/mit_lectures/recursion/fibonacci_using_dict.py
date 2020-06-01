''' Fibonacci series using dictionaries -
In this cas we use concept called memorization to store the
values and then using recursion to solve the complete problem.
Here it is more efficient and takes much smaller for computations '''


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}
print(fib_efficient(6, d))
print(d)
print(fib_efficient(20, d))

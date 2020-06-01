''' Fibonacci series using dictionaries -
In this case we use concept called memorization to store the
values and then using recursion to solve the complete problem.
Here it is more efficient and takes much smaller time for computations
A dictionary here can be used to store intermediate values that don't
change with each computations and thus can be reffred to in later steps
and hence increases the overall computation time '''


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

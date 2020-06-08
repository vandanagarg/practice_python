''' Examples - Linear Complexity '''


# example1
def add_digits(s):
    ''' searching a list in sequence to see if an element is present
        and add characters of a string '''
    val = 0
    for c in s:
        val += int(c)
    return val


# example2
def fact_iter(n):
    ''' find factorial using iterative calls '''
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


# example3
def fact_recur(n):
    ''' find factorial using recursive calls
        assume n >= 0 '''
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1)


# example4
def fib_iter(n):
    ''' iterative fibonacci '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

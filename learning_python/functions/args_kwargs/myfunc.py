def myfunc(*args):
    return [ num for num in args if num%2 == 0]

print(myfunc(10, 20, 30, 45))

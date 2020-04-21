###Timing your code # Timeit module

import timeit
# "0-1-2-3-.....-99"


print(timeit.timeit('"-".join(str(n) for n in range(100))', number= 10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number= 10000))  ##list comprehension usage
print(timeit.timeit('"-".join(map(str, range(100)))', number= 10000)) #using map function


def add2nums(a,b):
    return a+b

print(timeit.timeit('''def add2nums(a,b):
    return a+b
add2nums(3,1)'''))

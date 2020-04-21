import timeit


# setup = '''
import numpy as np

size = 3  # number of elements

a = np.arange(size)  # ndarray 
print(len(a))

l1 = list(range(size))  # list
print(len(l1))
# '''

# print(timeit.timeit('a+2', setup, number=2))
print(timeit.timeit('a+2', setup="from __main__ import a", number=7))

print(timeit.timeit('''import numpy as np
size = 3
a = np.arange(size)
a+2''', number=2))

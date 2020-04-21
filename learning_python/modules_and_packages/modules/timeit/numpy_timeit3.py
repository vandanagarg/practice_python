import timeit


def test():
    # setup ='''
    import numpy as np

    size = 3  # number of elements

    a = np.arange(size)  # ndarray 
    print(len(a))

    l1 = list(range(size))  # list
    print(len(l1))
    
    a+2
    # '''

# print(timeit.timeit('a+2', setup, number=2))
print(timeit.timeit("test()", setup="from __main__ import test", number=2))

print(timeit.timeit('''import numpy as np
size = 3
a = np.arange(size)
a+2''', number=2))

def test():
    c=0
    for i in range(100):
        c=i-c
    return c

print(test())


from timeit import Timer, timeit, repeat

print(__name__)
TimeIt = timeit("test()", setup="from __main__ import test", number=100000)
Repeat = repeat("test()", setup="from __main__ import test", repeat=3, number=100000)
print(TimeIt)
print(Repeat, min(Repeat))
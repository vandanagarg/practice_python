def factR(n):
    if n <= 1:
        return 1
    else:
        return n*factR(n-1)

def factI(n):
    prod = 1
    for i in range(2,n):
        prod = i*prod
    return prod

if __name__ == '__main__':
    import timeit

    ## 100
    print("Timeit with recursion for 100")
    print(timeit.timeit("factR(100)", setup="from __main__ import factR", number=1000))

    print("Timeit with iteration for 100")
    print(timeit.timeit("factI(100)", setup="from __main__ import factI", number=1000))

    ## 400
    print("Timeit with recursion for 400")
    print(timeit.timeit("factR(400)", setup="from __main__ import factR", number=1000))

    print("Timeit with iteration for 400")
    print(timeit.timeit("factI(400)", setup="from __main__ import factI", number=1000))
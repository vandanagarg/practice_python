''' Examples - Exponential Complexity
example: towers of hanoi, recursive fibonacci '''


# example1
def gen_subsets(L):
    ''' generating power sets '''
    res = []  # noqa: F841
    if len(L) == 0:
        return[[]]
    smaller = gen_subsets(L[: -1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

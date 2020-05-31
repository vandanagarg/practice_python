''' To find multiplication a*b using addition '''


def mult_iter(a, b):  # iterative approach
    result = 0
    while b > 0:  # iteration
        result += a  # current computation
        b -= 1  # iteration variable
    return result


print(mult_iter(4, 5))


def mult(a, b):  # recursive approach
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)


print(mult(4, 4))

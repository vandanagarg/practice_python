#generator to generate the square of numbers


def gensquares(N):
    for n in range(N):
        result = n**2
        yield result


for x in gensquares(10):
    print(x)


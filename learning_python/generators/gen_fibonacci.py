## fibonacci series


def gen_fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a,b = b, a+b


print(list(gen_fibonacci(10)))

for x in gen_fibonacci(10):
    print(x)


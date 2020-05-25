''' Scope details inside nested functions '''


def g(x):
    def h():
        x = 'abc'  # noqa: F841
    x = x + 1
    print("g: x =", x)
    h()
    return x


x = 3
z = g(x)
print(z)

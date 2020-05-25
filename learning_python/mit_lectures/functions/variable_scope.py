''' it explains different scopes for a variable '''


# example1:
# using same variable name in function and global scope
def f(y):
    x = 1
    x += 1
    print("inside function", x)


x = 5
f(x)
print("global scope", x)
print("\n")

# example2:
# only defining x in global scope but using it inside function as well
def g(y):  # noqa: E302
    print("inside function", x)
    print("inside function addition", x+1)


x = 5
g(x)
print("global scope", x)
print("\n")


# example3:
# only defining x in global scope but trying to modify it inside function
def h(y):
    x += 1  # gives error # noqa: F841, F823
    # UnboundLocalError: local variable 'x' referenced before assignment


x = 5
h(x)
print(x)

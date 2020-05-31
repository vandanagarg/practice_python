''' Tower of Hanoi -
There is stack in source tower, which needs to be shifted to
destination tower one by one. If needed we can even use spare tower
Here we have same base case and same arguments for all recursions '''


def printMove(n, fr, to):
    print("move", n, "from " + str(fr) + " to " + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(n, fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


# Towers(2, "source", "destination", "spare")
# Towers(1, "source", "destination", "spare")
Towers(3, "source", "destination", "spare")

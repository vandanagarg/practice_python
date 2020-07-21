# *args


def avg(*args):
    # print(args)
    s = sum(args)
    # print()
    l = len(args)
    return (round((s/l), 2))


print(avg(*[2, 5]))

l = [2, 6]
print(sum(l))

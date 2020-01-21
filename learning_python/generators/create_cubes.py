#generator functions allows us to write a  function that can send back a value and later
# resume to pick up where it left off , thus helps us to generate a sequence over time

# range(min, max, step size) is a generator step size by default is 1

def create_cubes(num):
    result = []
    for x in range(num):
        result.append(x**3)
    return result


print(create_cubes(5))
#now this o/p here stores the list of numbers returned in memory
# o/p:  [0, 1, 8, 27, 64]

#if we want the above list to not to be stored in memory but retun number one by one
# as nd when calculated we need to use generators


def create_cubes(num):
    for x in range(num):
        yield x**3


print(create_cubes(5))
print(list(create_cubes(5)))

for x in create_cubes(8):
    print(x)


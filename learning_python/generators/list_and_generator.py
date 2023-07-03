# This file shows the difference between list and generator expressions/comprehensions:

# list comprehension - denoted by square bractes []

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

print("list comprehension ", [x**2 for x in numbers if x%2 != 0])

# list comprehension generates output as soon as it is called and saves the result in memory

# generator expression - denoted by paranthesis (), it generates output only when called / required,
# thus it saves memory by not dumping the output immediately into the memory

numbers = [10, 13, 7, 11, 9, 14, 2, 8, 5, 6]

print('generator expression ', (x**2 for x in numbers if x%2 != 0))
# this generates a generator object which is callable 

gob = (x**2 for x in numbers if x%2 != 0)
# print("list(gob): ", list(gob))

for value in gob:
    print(value)

# n random numbers


import random


def rand_num(low, high, n):
    for num in range(n):
        rand_number = random.randint(low, high)
        yield rand_number


for number in rand_num(1,  10, 12):
    print(number)



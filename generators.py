#generator functions allows us to write a  function that can send back a value and later
# resume to pick up where it left off , thus helps us to generate a sequence over time

# range(min, max, step size) is a generator step size by default is 1

# def create_cubes(num):
#     result = []
#     for x in range(num):
#         result.append(x**3)
#     return result
#
# print(create_cubes(5))
#now this o/p here stores the list of numbers returned in memory
# o/p:  [0, 1, 8, 27, 64]

#if i want the above list to not to be stored in memory but retun number one by one
# as nd when calculated we need to use generators
# def create_cubes(num):
#     for x in range(num):
#         yield x**3
#
# print(create_cubes(5))
# print(list(create_cubes(5)))
#
# for x in create_cubes(8):
#     print(x)


## fibonacci series
# def gen_fibonacci(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         a,b = b, a+b
#
# print(list(gen_fibonacci(10)))
#
# for x in gen_fibonacci(10):
#     print(x)


# s = "hello"
# for letter in s:
#     print(letter)
#
# s_iter = iter(s)
# print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))

#1 generator to generate the square of numbers

# def gensquares(N):
#     for n in range(N):
#         result = n**2
#         yield result
#
# for x in gensquares(10):
#     print(x)


#2 n random numbers

# import random
#
# def rand_num(low, high, n):
#     for num in range(n):
#         rand_number = random.randint(low, high)
#         yield rand_number
#
# for number in rand_num(1, 10 , 12):
#     print(number)


#3 string to iterator
#
# s = "hello"
# s_iter = iter(s)
# print(s_iter)
# # print(list(s_iter))
# print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))

#4 use case of generator
# when we need not to store our o/p in memory nd only intention/usage is to loop through it we can use generators.

#5 explain gencomp
# my_list = [1,2,3,4,5]
# gencomp = (item for item in my_list if item > 3)
#
# print(gencomp)
# # print(list(gencomp))
#
# for item in gencomp:
#     print(item)

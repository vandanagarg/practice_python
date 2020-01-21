# use case of generator
# when we need not to store our o/p in memory nd only intention/usage is to loop through it we can use generators.

# explain gencomp

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)

print(gencomp)
# print(list(gencomp))


for item in gencomp:
    print(item)


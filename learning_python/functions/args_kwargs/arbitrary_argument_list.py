# using (*args) for using multiple arguments

def average(*args):
    return sum(args)/len(args)

print(average(5, 10))

print(average(5, 10, 15))

# creating a list and passing it as args argument, 
# it will internally unpack the elements of list grades and pass it as arguments in function average

grades = [15, 37, 92, 73, 88, 64]

print("grades passing as *args: ", average(*grades))

# creating a range and passing it as args argument, 
# it will internally unpack the elements of range and pass it as arguments in function average/calculate_product

print("range passed as *args: ", average(*range(0,6,2)))

def calculate_product(*args):
    final_product = 1
    for i in args:
        final_product *= i
    # print("final product is: ", final_product)
    return final_product

print("product of a given range is: ", calculate_product(*range(1,6,2)))

#count even numbers in a list

a= [1,2,3,4,5]

def count_even(a):
    count = 0
    for x in a:
        if x % 2 == 0:
            count += 1
    print("No. of even numbers: " + str(count))

count_even(a)
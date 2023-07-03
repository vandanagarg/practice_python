''' Using index() function to find index of a particular value and
    in/not in operator to find a particular value in a list '''

l = [0, 2, 3, 4, 6, 5, 3, 1]
''' index() function takes a value and passes the index position of that value in list/string/tuple
it can search a value within a particular index range
it gives exception in case a value is not present in the list
'''
print(l.index(2))

# in case of multiple occurences of a value it will give the first occurence index
print(l.index(3))

print(l.index(3, 3))

# print(l.index(7))  gives error

print(7 in l)
print(7 not in l)

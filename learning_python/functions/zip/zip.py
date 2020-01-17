a= ['a','b','c','d','e']
b = [1,3,3,4,5,5,6,77,4]
print(zip(a,b))

for items in zip(a,b):
    print (items)

print(list(zip(b,a)))
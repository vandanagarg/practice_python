####Advanced lists

l = [1,2,3,4]
print(l.count(10))
print(l.count(2))


x = [1,2,3]
x.append([4,5,6])
print(x)

x = [1,2,3]
x.extend([4,5,6])
print(x)

l.insert(2,"inserted")  #("index" ," object that we want to insert")
l.insert(5,"inserted")
l.insert(12,"inserted")
print(l.index("inserted"))
print(l)


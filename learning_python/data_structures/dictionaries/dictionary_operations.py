#basic operations on dictionaries

d = {'a':1, 'b':2}
print(d.items())
print(d.values())
print(d.keys())

print(d['a'])

d['c'] = 3
print(d)

d['c'] = d['c'] + 1
print(d)

for key, value in d.items():
    #print(items)
    print(key)
    print(value)


for item in d.items():
    print(item[1])

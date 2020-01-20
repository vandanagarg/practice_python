###Ordered dict - subclass of dictionary which remembers the order in which its contents are added
from collections import OrderedDict

d = {}
d['a'] =  1
d['b'] =  2
d['c'] =  3
d['d'] =  4
d['e'] =  5
print(d)
for k,v in d.items():
    print(k, v)


d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)

for k,v in d.items():
    print(k, v)

##normal dictionary
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

##ordered dict
# from collections import OrderedDict
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)


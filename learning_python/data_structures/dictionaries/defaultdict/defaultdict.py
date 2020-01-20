##defaultdict
# No key errors here

from collections import defaultdict
d= defaultdict(object)
print(d['one'])
for item in d:
    print(item)

d = defaultdict(lambda: 0)
print(d['one'])
print(d['three'])
d['two'] = 2
print(d)

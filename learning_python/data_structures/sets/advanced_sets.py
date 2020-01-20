##Advance Sets
s= set()
s.add(1)
s.add(2)
s.add(2)
s.add(3)
# print(s)
sc = s.copy()
# print(sc)
# s.clear()
# print(s)
# print(s.difference((sc)))

s.add(4)
# print(s.difference((sc)))


s1 = {1,2,3}
s2 = {1,4,5}
s3 = {6}

s1.difference_update(s2)  #removes the element from s1 which was common with set s2
print(s1)
print(s2)

s.discard(12)
print(s)

# intersection - common elements in sets a new set
print(s1.intersection(s))
print(s1.intersection(s2))

s1.intersection_update(s2)  #Here it updates the set s1 with the intersection result of set s1 with s2
print(s1)

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s1.issubset(s))
print(s.issuperset(s1))

print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)

print(s1.union(s2))
(s1.update(s2))
print(s1)


#counter - a dictionary subclass
from collections import Counter

# l = [1,1,1,1,1,1,1,6,656,526,5263,23,26,23,1,12,5,5,5,5,5,2,2,1,5,12,5,4,5,54,4,4,4]
# print(Counter(l))

# s = "vvvvvvvgggggppppsssjhfuekjksjdi"
# print(Counter(s))

s = "How may times does each word show up in this sentence word word show up up let's see ."

words= s.split()
print(Counter(words))

c= Counter(words)
print(c.most_common(4))

#total of all counts
print(sum(c.values()))

#reset all counts
# print(c.clear())

#list unique elements
print(list(c))

#convert to a set
print(set(c))

#convert to a regular dictionary
print(dict(c))

#convert to a list of (elem, cnt) pairs
list_of_pairs = c.items()
print(list_of_pairs)

#convert from a list of (elem, cnt) pairs
print(Counter(dict(list_of_pairs)))

#n least common elements
print(c.most_common()[: -n-1: -1]) #n any number  #define n first

#remove zero and negative counts
c += Counter()
print(c)


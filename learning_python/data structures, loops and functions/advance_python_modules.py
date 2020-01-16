# #counter - a dictionary subclass
# from collections import Counter
#
# # l = [1,1,1,1,1,1,1,6,656,526,5263,23,26,23,1,12,5,5,5,5,5,2,2,1,5,12,5,4,5,54,4,4,4]
# # print(Counter(l))
#
# # s = "vvvvvvvgggggppppsssjhfuekjksjdi"
# # print(Counter(s))
#
# s = "How may times does each word show up in this sentence word word show up up let's see ."
#
# words= s.split()
# print(Counter(words))
#
# c= Counter(words)
# print(c.most_common(4))
#
# #total of all counts
# print(sum(c.values()))
#
# #reset all counts
# # print(c.clear())
#
# #list unique elements
# print(list(c))
#
# #convert to a set
# print(set(c))
#
# #convert to a regular dictionary
# print(dict(c))
#
# #convert to a list of (elem, cnt) pairs
# list_of_pairs = c.items()
# print(list_of_pairs)
#
# #convert from a list of (elem, cnt) pairs
# print(Counter(dict(list_of_pairs)))
#
# #n least common elements
# print(c.most_common()[: -n-1: -1]) #n any number
#
# #remove zero and negative counts
# c += Counter()
# print(c)


###defaultdict
#No key errors here
# from collections import defaultdict
# d= defaultdict(object)
# print(d['one'])
# for item in d:
#     print(item)
#
# d = defaultdict(lambda: 0)
# print(d['one'])
# print(d['three'])
# d['two'] = 2
# print(d)


####Ordered dict - subclass of dictionary which remembers the order in which its contents are added

# d = {}
# d['a'] =  1
# d['b'] =  2
# d['c'] =  3
# d['d'] =  4
# d['e'] =  5
# print(d)
# for k,v in d.items():
#     print(k, v)


# from collections import OrderedDict
# d = OrderedDict()
#
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# d['e'] = 5
#
# print(d)
#
# for k,v in d.items():
#     print(k, v)

# ##normal dictionary
# d1 = {}
# d1['a'] = 1
# d1['b'] = 2
#
# d2 = {}
# d2['b'] = 2
# d2['a'] = 1
#
# print(d1 == d2)
#
# ##ordered dict
# from collections import OrderedDict
# d1 = OrderedDict()
# d1['a'] = 1
# d1['b'] = 2
#
# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1
#
# print(d1 == d2)
#


#####namedtuple

# from collections import namedtuple
#
# #here it is just similar to creating a quick class- thus it makes another object type and helps assigning names
# #Dog here is the class name inside brackets
# #sam is the variable name
# #In named tuple we need to pass 2 peremeters one is class name and another is the parameters or names that we need to pass
#
# Dog = namedtuple("Dog", "age breed name")
# sam = Dog(age = 2, breed= "Lab", name= "Sammy")
#
# print(sam.age)
# print(sam[2])
#
#
# Cat = namedtuple("Cat", "fur claws name")
# c = Cat(fur= 'fuzzy', claws=False, name ="kitty" )
#
# print(c.name)
# print(c[0])




########Datetime module

# import datetime
# # t = datetime.time(hour= 5, minute= 25, second= 1, microsecond= 3)
# # print(t)
# #
# # print(t.microsecond)
# # print(datetime.time.min)
# # print(datetime.time.max)
# # print(datetime.time.resolution)
# # print(datetime.time.tzinfo)
# #
# #
# # today = datetime.date.today()
# # print(today)
# #
# # print(today.timetuple())
# # print(today.day)
# # print(datetime.date.min)
# # print(datetime.date.max)
# # print(datetime.date.resolution)
#
# d1 = datetime.date(2015,3,11)
# print(d1)
#
# d2 = d1.replace(year = 1990)
# print(d2)
#
# print(d1- d2) # uses timedelta class



####Python debugger

# import pdb
#
# x = [1,2,3]
# y = 2
# z = 3
#
# result = y + z
# print(result)
#
# pdb.set_trace()
#
# result2 = y+x
# print(result2)


####Timing your code # Timeit module

# import timeit
# # "0-1-2-3-.....-99"
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number= 10000))
# print(timeit.timeit('"-".join([str(n) for n in range(100)])', number= 10000))  ##list comprehension usage
# print(timeit.timeit('"-".join(map(str, range(100)))', number= 10000)) #using map function



####StringIO

#in memory file like object . This object then can be used as i/p or o/p to most functions that would excpect a standard file object.

# from io import StringIO
#
# #arbitrary string
# message = " THis is just a normal message string."
#
# #Use StringIO method to set as file object.
# f = StringIO(message)
#
# #Now we have an object f that we will be able to treat just like a file .
# print(f.read())
#
# #Writing in a file
# f.write("\nsecond line written to file like object.")
#
# # reset cursor
# f.seek(0)
#
# #read again
# print(f.read())


###Advance python objects and data structures

##Advance numbers  # math library can

# print(hex(12))
# print(hex(512))
# print(hex(651))
# print(bin(1234))
# print(bin(128))
# print(bin(512))
#
# print(2**4)
# print(pow(2,4))
# print(pow(2,4,3))  ##(x**y) % Z
# print(abs(-3))
# print(abs(3))
# print(round(3.5))
# print(round(3.1))
# print(round(3.9))
# print(round(3.954656, 5))
# print(round(3.945456545, 3))


## Advanced Strings

# s = "Hello World"
# s= '  '
#changing cases

# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.count("o"))
# print(s.find("h"))
# print(s.find("z"))
# print(s.center(20," "))
# print("hello\thi")
# print("hello\thi".expandtabs(15))
# print(s.isalnum())
# print(s.islower())
# print(s.isspace())
# print(s.istitle())
# print(s.istitle())


##builting reg expresion
# print(s.split(" "))  #splits at every occurence
# print(s.partition("o"))  #splits at first occurence and returns the string with the seperator.



###Advance Sets
# s= set()
# s.add(1)
# s.add(2)
# s.add(2)
# s.add(3)
# # print(s)
# sc = s.copy()
# # print(sc)
# # s.clear()
# # print(s)
# # print(s.difference((sc)))
#
# s.add(4)
# # print(s.difference((sc)))
#
#
# s1 = {1,2,3}
# s2 = {1,4,5}
# s3 = {6}

# s1.difference_update(s2)  #removes the element from s1 which was common with set s2
# print(s1)
# print(s2)

# s.discard(12)
# print(s)

#intersection - common elements in sets a new set
# print(s1.intersection(s))
# print(s1.intersection(s2))
#
# s1.intersection_update(s2)  #Here it updates the set s1 with the intersection result of set s1 with s2
# print(s1)

# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))
# print(s1.issubset(s2))
# print(s1.issubset(s))
# print(s.issuperset(s1))

# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.union(s2))
# (s1.update(s2))
# print(s1)


###advanced dictionaries

# d = {"k1": 1, "k2": 2}
# print( {x : x**2 for x in range(10)})
# print( {k : v**2 for k,v in zip(["a","b"],range(2))})
#
# for k in d.items():
#     print(k)
#
# for k in d.values():
#     print(k)
#
# for k in d.keys():
#     print(k)
#
# print(d.values())
# print(d.items())
# print(d.keys())


#####Advanced lists

# l = [1,2,3,4]
# print(l.count(10))
# print(l.count(2))


# x = [1,2,3]
# x.append([4,5,6])
# print(x)

# x = [1,2,3]
# x.extend([4,5,6])
# print(x)

# l.insert(2,"inserted")  #("index" ," object that we want to insert")
# l.insert(5,"inserted")
# l.insert(12,"inserted")
# print(l.index("inserted"))
# print(l)


#### Test

#Problem 1: Convert 1024 to binary and hexadecimal representation
# print(hex(1024))
# print(bin(1024))

#Problem 2: Round 5.23222 to two decimal places
# print(round(5.23222,2))


#Problem 3: Check if every letter in the string s is lower case
# s = 'hello how are you Mary, are you feeling okay?'
# print(s.islower())
# for letter in s:
#     print(letter.islower())

#Problem 4: How many times does the letter 'w' show up in the string below?
# s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
# print(s.count("w"))

#Problem 5: Find the elements in set1 that are not in set2:
#Problem 6: Find all elements that are in either set:
# set1 = {2,3,1,5,6,8}
# set2 = {3,1,7,5,6,8}
# print(set1.difference(set2))
# print(set1.union(set2))

#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
# print({x:x**3 for x in range(5)})

#Problem 8: Reverse the list below:
# list1 = [1,2,3,4]
# list1.reverse()
# print(list1)
#
# #Problem 9: Sort the list below:
# list2 = [3,4,2,5,1]
# list2.sort()
# print(list2)

import collections
l= [17,8,9,10,0,1,2,3,4,5,6]
l = collections.deque(l)
# l.rotate(-4)
l.rotate(7)
print(l)
l = list(l)
l.sort()
print(l)
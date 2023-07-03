''' The function sorted() is used by mutable or immutable datatypes in which the given variable can he
iterated and it produces a list of elements in asc or desc order but function sort() is only used for lists '''

# using sort() function

l = [6, 4, 2,0, 3]
l.sort() # inbuilt function only for lists
print("l: ", l)

a = 'gxashwewq'
# a.sort() # gives error

# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# Cell In[6], line 1
# ----> 1 a.sort()

# AttributeError: 'str' object has no attribute 'sort'


# using sorted() function

l = [6, 4, 2,0, 3]

q = sorted(l)
print("q: ", q)
print("l: ", l)

w = sorted(a)
print("w: ", w)

u = 'shdhjsaSJGSDJHDFwiowowka xbx'
d = sorted(u)
print("d: ", d)

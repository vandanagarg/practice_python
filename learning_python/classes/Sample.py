
mylist = [1,2,3,4,4,5]

myset = set()

# myset.__dir__()
# mylist.extend()

print(type(mylist))
print(type(myset))

# o/p:
# <class 'list'>
# <class 'set'>

# everything in python is an object

# class  -- class keyword to create an user defined object

class Sample:
    def __init__(self,):
        pass
        # __init__ a method which will be called upon whenever we create an instance of this class

#instance of class
my_sample = Sample()

print(type(my_sample))
# <class '__main__.Sample'>

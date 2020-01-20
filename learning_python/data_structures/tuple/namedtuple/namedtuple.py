####namedtuple

from collections import namedtuple

#here it is just similar to creating a quick class- thus it makes another object type and helps assigning names
#Dog here is the class name inside brackets
#sam is the variable name
#In named tuple we need to pass 2 peremeters one is class name and another is the parameters or names that we need to pass

Dog = namedtuple("Dog", "age breed name")
sam = Dog(age = 2, breed= "Lab", name= "Sammy")

print(sam.age)
print(sam[2])


Cat = namedtuple("Cat", "fur claws name")
c = Cat(fur= 'fuzzy', claws=False, name ="kitty" )

print(c.name)
print(c[0])




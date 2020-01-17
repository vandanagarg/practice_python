# to see attributes of a class - breed is an attribute/characteristics of dog
#  self - instance of object itself

class Dog:
    # Class object attribute
    # same for any instance of a class
    # here we need not to use self keyword as it is not specific to an instance of a class but is generic

    species = "Mammal"

    def __init__(self, mybreed ,name, spots):  #constructor of class

        #attributes
        #we take in the arguments
        #assign it using self.attribute_name
        self.breed = mybreed
        #self.my_attribute = mybreed
        self.name =  name

        #Expect boolean True/False
        self.spots =  spots

    # Operations/ Actions --> Methods/ Methods is a function that is inside a class
    def bark(self,number):
        print("WOOF!")
        print("WOOF! My name is {} and house number is {}.".format(self.name, number))

my_dog = Dog( mybreed ='Lab', name = 'Tuffy', spots= "No Spots")  #instance of dog class

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(10)



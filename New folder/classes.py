# class NameOfClass(): #Camel Casing
#     def __init__(self,param1, param2):  #instance of the actual function
#         self.param1 = param1  # assigning self instances(actual instances of the class) the attributes the function
#         self.param2 = param2
#
# #some other functions
#     def some_method(self):  #use self to know that this is some method connected to a class
#         #perform some action
#         print(self.param1)


# mylist = [1,2,3,4,4,5]
#
# myset = set()
#
# # myset.__dir__()
# # mylist.extend()
#
# print(type(mylist))
# print(type(myset))
#
# o/p:
# <class 'list'>
# <class 'set'>

# everything in python is an object

# class  -- class keyword to create an user defined object

# class Sample():
#     def __init__(self,):
#         # __init__ a method which will be called upon whenever we create an instance of this class
#
# #instance of class
# my_sample = Sample()
#
# print(type(my_sample))
# # <class '__main__.Sample'>

# to see attributes of a class - breed is an attribute/characteristics of dog
#  self - instance of object itself

# class Dog():
#
#     # Class object attribute
#     # same for any instance of a class
#     # here we need not to use self keyword as it is not specific to an instance of a class but is generic
#
#     species = "Mammal"
#
#     def __init__(self, mybreed ,name, spots):  #constructor of class
#
#         #attributes
#         #we take in the arguments
#         #assign it using self.attribute_name
#         self.breed = mybreed
#         #self.my_attribute = mybreed
#         self.name =  name
#
#         #Expect boolean True/False
#         self.spots =  spots
#
#     # Operations/ Actions --> Methods/ Methods is a function that is inside a class
#     def bark(self,number):
#         print("WOOF!")
#         print("WOOF! My name is {} and house number is {}.".format(self.name, number))
#
# my_dog = Dog( mybreed ='Lab', name = 'Tuffy', spots= "No Spots")  #instance of dog class
#
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.spots)
# print(my_dog.species)
# my_dog.bark(10)



# class Circle():
#
#     # Class Object Attribute
#     PI = 3.14
#
#     def __init__(self, radius= 1):
#         self.radius = radius
#         self.area = radius*radius*self.PI  # self.pi can also be written as Circle.pi
#
#     #Method
#
#     def get_circumference(self):
#         return self.radius * self.PI * 2
#
# my_circle = Circle(30)
#
# print(my_circle.PI)
# print(my_circle.radius)
# print(my_circle.get_circumference())
# print(my_circle.area)




# class User():
#
#     def __init__(self,name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.addresses = []
#
#     def add_address(self, house_no, area, place):
#         self.house_no = house_no
#         self.area = area
#         self.place = place
#
#
#     def __str__(self):
#         print(" User name is: " + self.name)
#         print(" User email is: " + self.email)
#         print(" User age is: " + str(self.age))
#
#         for index in range(0,len(self.addresses)):
#             print(" User address " + str(index + 1) + " :")
#             address_index = self.addresses[index]
#             # print(address_index.house_no)
#             print("User House No. is :" + address_index.house_no)
#             print("User Area is : " + address_index.area)
#             print("User Place is : " + address_index.place)
#
# my_user = User("Vandana", "er.va", 27)
#
# home_address = User.add_address(my_user, "66", "ward 12", "Kurali")
# current_address = User.add_address(my_user, "0401", "str. praiser kommune", "Berlin")
# picky_address = User.add_address(my_user, "453", "Geeta Bhawan ", "Moga")
#
#
# my_user.__str__()

# class Address():
#
#     def __init__(self, house_no, area, place):
#         self.house_no = house_no
#         self.area = area
#         self.place = place
#
# print(home_address.(add_address("66", "ward 12", "Kurali")))
#
# print(current_address.add_address("0401", "str. praiser kommune", "Berlin"))
#
# picky_address = Address("453", "Geeta Bhawan ", "Moga")



# print(my_user.name)
# print(my_user.email)
# my_user.age = 28
# print( my_user.age)


# my_user.addresses.append(home_address)
# my_user.addresses.append(current_address)
# my_user.addresses.append(picky_address)



class Employee:  #Base class

    num_of_emps = 0
    raise_amt= 1.04

    def __init__(self, first, last,pay):
        self.first = first
        self.last =  last
        self.pay = pay
        # self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    #property decorator: define it like a method nd access it like an attribute
    #Getters, Setters, and Deleters

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    # now when we make fullname function to be used as attribute we remove (), which were earlier specifying that it is a  function
    #then if we try to assign a value to this attribute now it gives us an error and in order to resolve that error, that means
    #we should now be able to assign value to fullname attribute nd derive value out of it like to create a vice versa situation we use setter
    @fullname.setter
    def fullname(self, name):
        first, last  = name.split(" ")
        self.first = first
        self.last = last

    #to delete a particular code attribute
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #magic/ dunder methods
    def  __repr__(self):
        return "Employee ('{}', '{}', {})". format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}". format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())





    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        pass

emp1 = Employee("Vandana", "Garg", 60000)
emp2 = Employee("Peeyush", "Singla", 70000)

emp_str_1 = "Vandana-Singla-60000"
new_emp_1 = Employee.from_string(emp_str_1)
#
# print(Employee.fullname(new_emp_1))
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
#
# Employee.set_raise_amt(1.05)
# # emp1.set_raise_amt(1.05)
#
# print(Employee.__dict__)
# print(emp1.__dict__)
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
#
# emp1.raise_amt = 1.06
#
# print(emp1.raise_amt)
# print(emp1.__dict__)
#



# class/instance.__dict__



##################################################
# Inheritance -   we can use the existing class nd reuse the code
#
# class Employee:
#
#     def __init__(self, first, last, pay):
#         pass

class Developer(Employee):  #derived class

    def __init__(self, first, last,pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):  # derived class

    def __init__(self, first, last,pay, employees= None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())



dev_1 = Developer("Corey", "Schafer", 40000, "Python")
dev_2 = Developer("Test", "User", 50000, "Java")


mgr_1 = Manager("Sue", "Smith", 980000, [dev_1])


#if object is instance of a class

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
#
# print(issubclass(Manager, Developer))
# print(issubclass(Developer, Employee))

# print(mgr_1.email)
# print(mgr_1.employees)
#
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
#
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.prog_lang)

# print(emp1)
# print(emp2)

# print(repr(emp1))
# print(str(emp1))
#
# print(emp1.__repr__())
# print(emp1.__str__())
#
# print(int.__add__(1,2))
# print(str.__add__("a", "b"))
#
# print(emp1 + emp2)
# print(len(emp1))


# o/p : <__main__.Employee object at 0x0000000000670648>
# <__main__.Employee object at 0x0000000000670688>

#o/p:
# Employee ('Vandana', 'Garg', 60000)
# Vandana Garg  - Vandana.Garg@company.com
# Employee ('Vandana', 'Garg', 60000)
# Vandana Garg  - Vandana.Garg@company.com
# 3
# ab
# 130000
# 13

# emp1.first = "Peeyush"

emp1.fullname = "Vandana Singla"

print(emp1.first)
print(emp1.fullname)
print(emp1.email)

del emp1.fullname

print(emp1.first)
print(emp1.fullname)
print(emp1.email)
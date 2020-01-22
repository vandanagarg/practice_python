class Employee:  #Base class

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
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
            print("-->", emp.fullname)



dev_1 = Developer("Corey", "Schafer", 40000, "Python")
dev_2 = Developer("Test", "User", 50000, "Java")


mgr_1 = Manager("Sue", "Smith", 980000, [dev_1])


# if object is instance of a class

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Developer))
print(issubclass(Developer, Employee))

print(mgr_1.email)
print(mgr_1.employees)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(help(Developer))
print(dev_1.email)
print(dev_2.email)
print(dev_1.prog_lang)

#
# emp1.first = "Peeyush"
#
# emp1.fullname = "Vandana Singla"
#
# print(emp1.first)
# print(emp1.fullname)
# print(emp1.email)
#
# del emp1.fullname
#
# print(emp1.first)
# print(emp1.fullname)
# print(emp1.email)
#
#
# print(emp1)
# print(emp2)
#
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

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
        first, last = name.split(" ")
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

# print(Employee.fullname(new_emp_1))

print(new_emp_1.email)
print(new_emp_1.pay)

Employee.set_raise_amt(1.05)
emp1.set_raise_amt(1.05)

print(Employee.__dict__)
print(emp1.__dict__)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp1.raise_amt = 1.06

print(emp1.raise_amt)
print(emp1.__dict__)


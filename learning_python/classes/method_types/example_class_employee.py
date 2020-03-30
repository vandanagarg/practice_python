import datetime


class Employee:  # Base class

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Vandana", "Garg", 60000)
emp2 = Employee("Peeyush", "Singla", 70000)

emp_str_1 = "Vandana-Singla-60000"
new_emp_1 = Employee.from_string(emp_str_1)

# print(Employee.fullname(new_emp_1))

print(new_emp_1.email)
print(new_emp_1.pay)

Employee.set_raise_amt(1.05)
emp1.set_raise_amt(1.05)

print(Employee.__dict__)  # To print namespace of Employee
# Namespace tells what all values/variables this class has acess to
print(emp1.__dict__)
# Here namespace tells what all values/variables this instance has access to
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp1.raise_amt = 1.06

print(emp1.raise_amt)
print(emp1.__dict__)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

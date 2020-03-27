# Two type of variables:
# Instance variables
# Class variables


class User:

    counter = 0  # class variable

    def __init__(self, name, email):
        self.name = name  # instance variable
        self.email = email  # instance variable

    def send_email(self):
        User.counter += 3
        return self.email

    def show_repr(self):
        return self

    def __repr__(self):
        User.counter += 1
        return f"Name is {self.name} and email id is {self.email}."

    @classmethod
    def print_count(cls):
        print(User.counter)


print("\n1. send_email\n")

print(User("vandana", "er.vandana").send_email())
print(User("p", "peyush").send_email())
print(User("ps", "singla").send_email())
print(User("vs", "vsingla").send_email())

print("\n2. show_repr\n")

print(User("vandana", "er.vandana").show_repr())
print(User("p", "peyush").show_repr())
print(User("ps", "singla").show_repr())
print(User("vs", "vsingla").show_repr())

print("\n3. __repr__\n")
# using __repr__ built in method to return and print output
print(User("vandana", "er.vandana"))
print(User("p", "peyush"))
print(User("ps", "singla"))
print(User("vs", "vsingla"))

print("\n4. Total count")
print(User.counter)
User.print_count()

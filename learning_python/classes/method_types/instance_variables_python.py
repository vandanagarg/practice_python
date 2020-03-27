# Two type of variables:
# Instance variables
# Class variables


class User:

    counter = 0  # class variable

    def __init__(self, email):
        self.email = email  # instance variable

    def send_email(self):
        User.counter += 1
        print(self.email)

    def __repr__(self):
        User.counter += 2
        return (self.email)

    @classmethod
    def print_count(cls):
        print(User.counter)


User("er.vandana").send_email()
User("peyush").send_email()
User("singla").send_email()
User("vsingla").send_email()

# using __repr__ built in method
print(User("er.vandana"))
print(User("peyush"))
print(User("singla"))
print(User("vsingla"))

print(User.counter)
User.print_count()

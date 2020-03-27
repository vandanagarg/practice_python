# Two type of variables:
# Instance variables
# Class variables


class User:

    counter = 0  # class variable

    @classmethod
    def send_email(cls, email):
        User.counter += 1
        print(email)


User.send_email("er.vandana")
User.send_email("peyush")
User.send_email("singla")
print(User.counter)

''' Defining Parent Class for inheritance examples '''


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    # creating getter methods
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # creating setter methods
    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

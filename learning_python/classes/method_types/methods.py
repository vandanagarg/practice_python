class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "classmethod called", cls

    @staticmethod
    def staticmethod():
        return "static method called"

class MyClass:
    def method(self):
        print("instance method called", self)

    @classmethod
    def classmethod(cls):
        print("classmethod called", cls)

    @staticmethod
    def staticmethod():
        print("static method called")


obj = MyClass()

obj.method()
# instance method called <__main__.MyClass object at 0x10eb28940>

obj.classmethod()
# classmethod called <class '__main__.MyClass'>

obj.staticmethod()
# static method called

MyClass.classmethod()
# classmethod called <class '__main__.MyClass'>

MyClass.staticmethod()
# static method called

MyClass.method()
# TypeError: method() missing 1 required positional argument: 'self'

# TypeError: unbound method method() must be called with MyClass instance as
# first argument (got nothing instead)

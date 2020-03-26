# Method Types OOP Python

* Plain/Regular methods or Instance methods

object instance/ argument (self)
:white_check_mark: Can modify object instance state / Has access to object instance
:white_check_mark: Can modify class state / Has access to class

* Class methods

class instance/ argument (cls)
:negative_squared_cross_mark: Can't modify object instance state / Has no access to object instance
:white_check_mark: Can modify class state (cls) / Has access to class

* Static methods

no instance/ no arguments
:negative_squared_cross_mark: Can't modify object instance state / Has no access to object instance
:negative_squared_cross_mark: Can't modify class state / Has no access to class

*When to use?*
Since static method doesn't have access to class or object instance at all.
It doesn't change any of them and is a self contained method.
It's a way to namespace our function.

Example:

"""python

class D:
    def instance_method(self, x, y):
        pass

    @staticmethod
    def static_method(x, y):
        pass

    @classmethod
    def cls_method(cls, x, y):
        pass


d = D()
d.instance_method(1, 2)  # like a normal function
instance_method(d, 1, 2)

d.static_method(1, 2)
static_method(1, 2)

d.cls_method(1, 2)
cls_method(type(d), 1, 2)  # checks type of d

D.cls_method(1, 2)
cls_method(D, 1, 2)
# here function has no need to check type of d and knows the class directly
# from where it has been  called.

"""
#A combination of args and kwargs

def pass_values(*args, **kwargs):  #order matters so *args is positional argument but **kwargs is keyword argument
    print(args)
    print(kwargs)
    print ("I would like {} {}.".format(args[0], kwargs['food']))

pass_values(10, 20, 30, fruits='apple', food='eggs', juice='orange')


class NameOfClass(): #Camel Casing
    def __init__(self,param1, param2):  #instance of the actual function
        self.param1 = param1  # assigning self instances(actual instances of the class) the attributes the function
        self.param2 = param2

#some other functions
    def some_method(self):  #use self to know that this is some method connected to a class
        #perform some action
        print(self.param1)


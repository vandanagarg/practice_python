class Student:  #buiding attributes for student class

    def __init__(self, name, major, gpa, is_on_probation):  #this init function is describing what a student has, like how we want to describe a student
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


#class is basically an overview of what student datatype is
#and an object is an actual student represented inside our program
#now we have to call this filefrom our actual file/program
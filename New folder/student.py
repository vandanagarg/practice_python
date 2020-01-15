class Student:  #buiding attributes for student class

    #def __init__(self, name, major, gpa, is_on_probation):  # this init function is describing what a student has, like how we want to describe a student
    def __init__(self, name, major, gpa):  #this init function is describing what a student has, like how we want to describe a student
        self.name = name
        self.major = major
        self.gpa = gpa
       # self.is_on_probation = is_on_probation

    def on_honor_roll(self):       #for object function we just add a small function in here
        if self.gpa >= 3.5:
            return True
        else:
            return False

#class is basically an overview of what student datatype is
#and an object is an actual student represented inside our programm and is no more a
#now we have to call this filefrom our actual file/programm




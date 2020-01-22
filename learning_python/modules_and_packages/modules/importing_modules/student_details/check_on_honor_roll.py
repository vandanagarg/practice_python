#Object Functions #function in classes
#class functions is something that can be used within the class and can be used to modify objects of that class

from student import Student

student1 = Student("van", "Maths", 3.8)
student2 = Student("PS", "science", 3.1)

print(student2.on_honor_roll())
print(student1.on_honor_roll())


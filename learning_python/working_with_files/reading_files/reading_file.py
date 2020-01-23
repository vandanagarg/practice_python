# Reading Files
# to read files outside the python

#making a variable to open a file and store it
employee_file = open("employees.txt", "r")

# if the file happens to be in same directory in which we are working then we can just give the file name directly
''' 3 modes to open a file "r" just to read, "w" just to write, "a" to appends, here basically we cant write anything, change anythings but
can just appends i.e: add something at the end of the file, "r+" it gives the access to read nd write as well.
'''

print(employee_file.readable())  # this is to check if this file is even readable or not and this is going to return a boolean value
# since here we have selected read mode i.e: r its should return True , if its in any other mode it will give o/p as False,
# only for 2 modes i.e: r and r+ the readable function will give the o/p as True

# o/p
# True

#now to actually read the file
print(employee_file.read())  # will read whole file at once

# o/p
# Jim - Salesman
# Dwight - Salesman
# Pam - Receptionist
# Michael - Manager
# oscar - Accountant


#to read line by line
print(employee_file.readline())  #so what it does it starts reading from first line nd shifts the cursor to next line in next run nd thus next line will be printed

# o/p
# Jim - Salesman

print(employee_file.readline())
print(employee_file.readline())

# o/p
# Jim - Salesman
#
# Dwight - Salesman

#or we can use another function readlines in order to print lines ; what it does is it takes all the lines and put them in an array(by array it means list)
# now when we print that function what we get is an array

print(employee_file.readlines())

# o/p
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# ['Jim - Salesman\n', 'Dwight - Salesman\n', 'Pam - Receptionist\n', 'Michael - Manager\n', 'oscar - Accountant']



print(employee_file.readlines(1))  # to access a specific line we need to pass the index

# o/p
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# Dwight - Salesman



#we can even use a for loop to print individual lines

for employee in employee_file.readlines():
    print(employee)

# o/p
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# Jim - Salesman
#
# Dwight - Salesman
#
# Pam - Receptionist
#
# Michael - Manager
#
# oscar - Accountant




#now if we are opening a  file we must close it as well

employee_file.close()  # now we can no longer access the file


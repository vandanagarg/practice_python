#writing to a file

employee_file = open("employees.txt", "a")  #adding text to the end of the file

employee_file.write("\nkelly - HR ")  #nothing shows up in the console, but if u check in file it adds there
#but be carefull if u happen to run again it appends in file twice

# now where and how it appends it depends , if we have a new line space in our file it will append in the next line
# if we don't have a new line space in our file its going to append in the same line like in the end in sequence
# so if we want it to come in new line we must give a new line character "\n " to tell it to go in new line
# but if we give a new line character and it has already one line space in file then it skips one line and prints in next line

#to create a new file -- it creates a new file same as employess.txt
#we can create any sort of file for eg: html, xml etc
employee_file = open("employees1.txt", "w")

#now if we use w , instead of appending the file what it does is it over-rides the file .i.e: it replaces all contents of file with the new content we wish to add
employee_file = open("employees1.txt", "w")
employee_file.write("kelly - HR ")

#now if we are opening a  file we must close it as well

employee_file.close()  # now we can no longer access the file



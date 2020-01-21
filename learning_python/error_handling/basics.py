#try -  Block that may lead to error
#except - this block of code will execute in case there is any error in try block and then it falls into except block
#finally - final block of code to be executed always; regardless of an error

try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass


#example-1
try:
    #want to attempt this code
    #may have an error
    result = 10+ 10
    # print(result)
except:
    #to print/return in case of error
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)



#example-2
try:
    f = open("testfile","r")  # open a file in w mode or create a new file
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:  #permission error
    print("Hey you have an OS error.")
finally:
    print("I always run.")


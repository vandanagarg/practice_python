#try -  Block that may lead to error
#except - this block of code will execute in case there is any error in try block and then it falls into except block
#finally - final block of code to be executed always; regardless of an error
#
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# try:
#     #want to attempt this code
#     #may have an error
#     result = 10+ 10
#     # print(result)
# except:
#     #to print/return in case of error
#     print("Hey it looks like you aren't adding correctly!")
# else:
#     print("Add went well!")
#     print(result)


# try:
#     f = open("testfile","r")  # open a file in w mode or create a new file
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error!")
# except OSError:  #permission error
#     print("Hey you have an OS error.")
# finally:
#     print("I always run.")


# def ask_for_int():
#     try:
#         result = int(input("Please provide number: "))
#     except:
#         print("ohh! this is not a number.")
#     finally:
#         print("End of try/except/finally.")

#
# def ask_for_int():
#     while True:
#         try:
#             result = int(input("Please provide number: "))
#         except:
#             print("ohh! this is not a number.")
#             continue
#         else: #means there is no exception and user entered a correct int value
#             print("Yes thank you.")
#             break  #goes up-to its enclosing loop here while loop
#         finally:  # here we can even put a finally block of code after else otherwise we can just keep either of these
#             # but include break statement uin that in order to come out of infinite loop
#             print("End of try/except/finally.")
#             print("I will always run at the end!")
#
# ask_for_int()

# try:
#     f= open("test_file.txt")
#     var = bad_var
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
#
# #o/p:
# # [Errno 2] No such file or directory: 'test_file.txt'
# #name 'bad_var' is not defined

##manually raising exceptions
# try:
#     f= open("currupt_file.txt")
#     if f.name == "currupt_file.txt":
#         raise Exception
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print("Error!")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally...")


#problem 1

# try:
#     for i in ["a","b","c"]:
#         print(i**2)
# except TypeError:
#     print("Please pass a valid list of integers.")
# except:
#     print("Opps, you have passed some wrong value.")
# finally:
#     print("End of the program..")
#
#
# #problem 2
#
# try:
#     x= 5
#     y= 0
#     z= x/y
# except ZeroDivisionError:
#     print("Oh dear division by zero is not allowed as per maths :) try again!!")
# except :
#     print("Something went wrong.")
# finally:
#     print("All done.")

#problem 3
# def square_int():
#     while True:
#         try:
#             num_input = int(input("Enter a number: "))
#             result = num_input ** 2
#         except ValueError:
#             print("Oh you have not entered a correct integer value.")
#         except Exception as e:
#             print(e)
#             continue
#         else:
#             print("Square of your number is: " + str(result))
#             break
#         # finally:
#         #     print("End of the program...")
#
# square_int()



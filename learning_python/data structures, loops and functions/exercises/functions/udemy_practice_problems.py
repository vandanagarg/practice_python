# #A combination of both
#
# def myfunc(*args, **kwargs):  #order matters so *args is positional argument but **kwargs is keyword argument
#     print(args)
#     print(kwargs)
#     print ("I would like {} {}.".format(args[0], kwargs['food']))
#
# myfunc(10, 20, 30, fruits='apple', food='eggs', juice='orange')



# def myfunc(*args):
#     return [ num for num in args if num%2 == 0]
#
# print(myfunc(10, 20, 30, 45))

# def square_num(num):
#     return num ** 2
#
# num = [4556,54,545,45,54,4,5,2]
#
# print(list(map(square_num, num)))


# square =  lambda num: num ** 2   # no name here how does below work ?
# print(square(5))

# my_nums= [10, 20, 30, 45]
# print(list(map(lambda num: num ** 2 ,my_nums)))
#
# print(list(filter(lambda num : num% 2 == 0, my_nums)))
#
# names = ['Andy', 'vandana garg', 'Eve', 'Sally']
#
# print(list(map(lambda name: name[:: -1],names)))


# name = 'A global string'
#
# def greet():
#
#     # name = 'Vandana'
#
#     def hello():
#
#         #name = 'I am local'
#
#         print('Hello ' +  name)
#     hello()
# greet()


#
# def sum_numbers(*args):
#     total = 0
#     for nums in args:
#         total = total + nums
#     return total
#
# print(sum_numbers(5,6,5,8,52,2))
#
# import datetime
# def user_age():
#     input_user_age = int(input("Enter your age: "))
#     #print(input_user_age)
#
#     now = datetime.datetime.now()
#     current_year = now.year
#
#     diff_age = 100 - input_user_age
#     year_100 = current_year + diff_age
#
#     return ("You will be of 100years in year " + str(year_100) + " .")
#
# print(user_age())

# 95  2019 + 5
# 2024

# def check_even_odd(num):
#     return num % 2 == 0
#
# print(check_even_odd(567))
#
# def film_category():
#     user_age = int(input("Enter your age : "))
#     print(user_age)
#
#     if user_age in range (0,13):
#         return "You can not watch any film."
#     elif user_age in range (13, 19):
#         return "You can watch animated movies. "
#     else :
#         return "You can watch any movie. "
#
# print(film_category())


# def remove_small_element():
#     num = 6
#     num_list = [5,89,56,4,8,2,4,1,100]
#     print(len(num_list))
#     #
#     # for i in range (0, len(num_list)):
#     #     if num_list[i] < 6:
#     #         num_list.pop(i)
#     #     else:
#     #         continue
#     # return num_list
#
# print(remove_small_element())

#remove_small_element()

# list_ex = [56,8,5,8,114,158,2,1]
#
# print(list_ex.pop(0))
# print(list_ex)



# def remove_small_element():
#     num = 6
#     num_list = [5,89,56,4,8,2,4,1,100]
#     new_list = []
#
#     for i in range (0, len(num_list)):
#         if num_list[i] > int(num):
#             new_list.append(num_list[i])
#             #print(num_list[i])
#
#     return new_list
#
# print(remove_small_element())



#Q1: volume of sphere 4/3 * pie * r**3

# def vol(rad):
#     return 4/3 * 3.14 * (rad ** 3)
#
# print(vol(0))
# print(vol(1))

#Q2:  number in range

# def ran_check(num, low, high):
#     return  high >= num >= low

# def ran_check(num, low, high):
#     if high >= num >= low:
#         return "The given number is within the range."
#     else:
#         return "The given number is not within the range."
#
# print(ran_check(5,2,9))
# print(ran_check(8,2,7))

#print nd bool chk

#Q3:   upper nd lower case in a sentence

# def up_low(inp_string):
#     lower_count = 0
#     upper_count = 0
#
#     for letter in inp_string:
#         if letter in "abcdefghijklmnopqrstuvwxyz":
#             lower_count += 1
#         elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#             upper_count += 1
#         else:
#             continue
#     print("Count of letters in Upper case is: " + str(upper_count))
#     print("Count of letters in lower case is: " + str(lower_count))
#
# up_low("Hello, I am Vandana Garg.")


#Q4: return a unique list:

# inp_list = [2,5,2,5,2,5,6,8,6,8,7,9,9,2,1,0]
# unique_lst = []
#
# def unique_list(inp_list):
#     for item in inp_list:
#         if item in unique_lst:
#             continue
#         else:
#             unique_lst.append(item)
#     return unique_lst
#
# print(unique_list(inp_list))


#Q5:  multiply all numbers in a list

# numbers = [2,5,8,4]
#
# def multiply(numbers):
#     mul_result = 1
#     for item in range(0, len(numbers)):
#         mul_result = mul_result * int(numbers[item])
#     return mul_result
#
# print(multiply(numbers))


# #Q6:  chk palindrome

# def palindrome(inp_string):
#     inp_new_string = inp_string.replace(" ", "")
#     #print(inp_new_string)
#     reverse_string = inp_new_string[:: -1]
#     if inp_new_string == reverse_string:
#         return "The input string is a palindrome."
#     else:
#         return "The input string is not a palindrome"
#
# print(palindrome("hello"))
# print(palindrome("nurses run"))

#Q7: check pangram
#
# import string
# #print(string.ascii_lowercase)
#
# def ispangram(inp_string):
#     alphabets = string.ascii_lowercase
#     for letter in alphabets:
#         if letter in inp_string:
#             #print(letter)
#             result = "True"
#         else:
#             #print("Else " + str(letter))
#             result = "False"
#             break
#     return result == 'True'
# #
#
# import string
#
#
# def chk_letters(inp_str):
#     alphabet = string.ascii_lowercase
#     missing_letters = []
#     for letter in alphabet:
#         if letter in inp_str:
#             continue
#         else:
#             missing_letters.append(letter)
#     return missing_letters
#
# print(chk_letters("he quick brown fox jumps  t lazy dog"))

# print(ispangram("he quick brown fox jumps v t lazy dog"))
#ispangram("The ")

#print(5 in range (2,6))

#set()

# import string
# # def ispangram(str1, alphabet = string.ascii_lowercase):
# #     alphaset = set(alphabet)
# #     #print(alphaset)
# #     # alphaset <= set(str1.lower())
# #     # print(set(str1.lower()))
# #     return alphaset <= set(str1.lower())
# #
# #
# # print(ispangram("vandana"))






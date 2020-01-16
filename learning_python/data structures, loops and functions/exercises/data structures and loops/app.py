# # #to get count of all letters in a string.
# from collections import Counter
#
# # initializing string
# test_str = "GeeksforGeeks. *"
# #taking input from user
# test_str = input("Enter a string : ")
# # Enter a string : Vandana Garg loves Peeyush Singla a lot :* :* :)
# # using collections.Counter() to get count of each element in string
# res = Counter(test_str)
#
# # printing result
# print("Count of all characters in the string is :\n " + str(res))
# print("\nCount of G in the string is : " + str(res["G"]))
#
# counter= test_str.count("e")
# print("\ncount is : "+ str(counter))
#
# #
# # weekday = True
# # vacation = True
# #
# # def sleep_in(weekday, vacation):
# #     if not weekday and not vacation:
# #         return True
# #     elif weekday == True and not vacation:
# #         return False
# #     elif not weekday and vacation == True:
# #         return True
# #     else:
# #         return False
# #
# #
# # print(sleep_in(False, True))
#
#
# # #2
# # def string_times (str,n):
# #     return str * n
# #
# # print(string_times("Hi",3))
# #
# # #3
# #
# #
# # def string_name (name):
# #     print("Hello " + name + " !")
# #
# # string_name(input("Enter your name: "))
#
#
# #4
# # a = [1,2,5]
# # def first_last6 (a):
# #         #if a[0] or a[len(a) - 1]  == 6:
# #         if a[0]== 6 or a[- 1]  == 6:
# #             return True
# #         # else:
# #         #     return False
# #
# # print(first_last6(a))
#
#
# # #5  d='abc'  d = d + 'f' or d += 'f' (shortcut) (to add the strings)  ???? just last output
# #
# # # #a = 'ABC'
# # #
# # def double_char(a):
# #     to_return = ''
# #     for c in a:
# #         to_return += c*2
# #     print(to_return)
# #        # return to_return
# #
# # double_char("ABC")
# # #print(double_char("ABC"))
# # #
# # # o/p is :
# # #
# # C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# # AA
# # AABB
# # AABBCC
# #
# #
# # # o/p is :
# # C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# # AA
#
#
# # #6
# # a= [1,2,3,4,5]
# #
# # def count_even(a):
# #     count = 0
# #     for x in a:
# #         if x % 2 == 0:
# #             count += 1
# #     print("No. of even numbers: " + str(count))
# #
# # count_even(a)


#print("Hello")

#
# #a = 'ahcjudncjudjjhlpsvgaa'
# a = 'aabbccdddeeepppsssvvvvggggllllll'
# d = {}
#
# for letter in a:
#     #d_items = d.keys()
#     #print([0][0])
#     #print(letter)
#     if letter in d.keys():
#         d[letter]  += 1
#     else:
#         d[letter] = 1
# print (d)




# d = {'a':1, 'b':2}
# print(d.items())
# print(d.values())
# print(d.keys())
#
# print(d['a'])
#
# d['c'] = 3
#print(d)
#
# d['c'] = d['c'] + 1
# print(d)

# for key, value in d.items():
#     #print(items)
#     print(key)
#     print(value)


# for item in d.items():
#     print(item[1])

# word = 'abcde'
#
# for item in enumerate(word):
#     print(item[1])

# a= ['a','b','c','d','e']
# b = [1,3,3,4,5,5,6,77,4]
# print(zip(a,b))

# for items in zip(a,b):
#     print (items)

# print(list(zip(b,a)))

#2 list with marks of students of eng and maths, add the list using zip and store sum of 2 lists in that.=  ques  to solve

num_maths = [3,32,35,56,6,77,3,13,54,65,67,63]
num_eng =[54,56,45,4,4,5,11,55,1,24,55,11,55,45]
total_marks = []
combine_lists = zip(num_maths,num_eng)
print(combine_lists)

for item in zip(num_maths,num_eng):
    total_marks.append(item[0] + item[1])
   # print (total_marks)

print (total_marks)

#total_marks = num_maths + num_eng
#print(total_marks)

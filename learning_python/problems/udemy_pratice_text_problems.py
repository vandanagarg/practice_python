#Problem 1
# Fizz Buzz - Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

# def fizzbuzz():
#     for i in range(1,101):
#         if i % 3 ==0 and i % 5 ==0:
#             print("FizzBuzz")
#         elif i % 3 ==0 :
#             print("Fizz")
#         elif i % 5 ==0:
#             print("Buzz")
#         else:
#             print(i)
#
# fizzbuzz()


######################
# Problem 2
# Reverse a String - Enter a string and the program will reverse it and print it out.


# a = "vandana"
# print(a[::-1])
#
# def reverse(string):
#     string = "".join(reversed(string))
#     return string
#
# print(reverse("peeyush"))
#
#
# str = "Python" # initial string
# reversedString=[]
# index = len(str) # calculate length of string and save in index
# while index > 0:
#     reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
#     index = index - 1 # decrement index
# print(reversedString)
# print("".join(reversedString))


####################################
# Problem 3
#Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant
# sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

# Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

# Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
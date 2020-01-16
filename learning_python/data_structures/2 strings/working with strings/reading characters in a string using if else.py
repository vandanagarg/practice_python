#problem statement : to get count of all letters in a string.

from collections import Counter

#taking input from user
test_str = input("Enter a string : ")

#using if else
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
# printing result
print("Count of all characters in the string is :\n " + str(all_freq))


#output:
#just lower case input/output no special characters.
#
# Enter a string : iamgood
# Count of all characters in the string is :
#  {'i': 1, 'a': 1, 'm': 1, 'g': 1, 'o': 2, 'd': 1}
#
#  #with special characters and upper case
#  Enter a string : I am good :)
# Count of all characters in the string is :
#  {'I': 1, ' ': 3, 'a': 1, 'm': 1, 'g': 1, 'o': 2, 'd': 1, ':': 1, ')': 1}

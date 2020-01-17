#to get count of all letters in a string.
from collections import Counter

# initializing string
test_str = "GeeksforGeeks. *"

#taking input from user

test_str = input("Enter a string : ")
# Enter a string :
# using collections.Counter() to get count of each element in string
res = Counter(test_str)

# printing result
print("Count of all characters in the string is :\n " + str(res))
print("\nCount of G in the string is : " + str(res["G"]))

counter= test_str.count("e")
print("\ncount is : "+ str(counter))

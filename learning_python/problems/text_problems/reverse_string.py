# Problem 2
# Reverse a String - Enter a string and the program will reverse it and print it out.

#1st way
a = "vandana"
print(a[::-1])


#2nd way
def reverse(string):
    string = "".join(reversed(string))
    return string

print(reverse("peeyush"))


#3rd way
str = "Python" # initial string
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0:
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString)
print("".join(reversedString))



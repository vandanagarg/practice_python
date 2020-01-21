#Q7: check pangram

import string
#print(string.ascii_lowercase)

def ispangram(inp_string):
    alphabets = string.ascii_lowercase
    for letter in alphabets:
        if letter in inp_string:
            #print(letter)
            result = "True"
        else:
            #print("Else " + str(letter))
            result = "False"
            break
    return result


print(ispangram("Vandana"))
print(ispangram("he quick brown fox jumps v t lazy dog"))
print(ispangram("The "))


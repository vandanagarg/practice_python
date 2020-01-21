#check pangram using set()

import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    #print(alphaset)
    # alphaset <= set(str1.lower())
    # print(set(str1.lower()))
    return alphaset <= set(str1.lower())


print(ispangram("vandana"))
print(ispangram("he quick brown fox jumps v t lazy dog"))


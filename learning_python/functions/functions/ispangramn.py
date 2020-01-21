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
    return True

print(ispangram("Vandana"))


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




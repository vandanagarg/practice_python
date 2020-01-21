#Q6:  chk palindrome

def palindrome(inp_string):
    inp_new_string = inp_string.replace(" ", "")
    #print(inp_new_string)
    reverse_string = inp_new_string[:: -1]
    if inp_new_string == reverse_string:
        return "The input string is a palindrome."
    else:
        return "The input string is not a palindrome"


print(palindrome("hello"))
print(palindrome("nurses run"))


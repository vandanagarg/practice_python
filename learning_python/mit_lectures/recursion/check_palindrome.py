''' for non numerics or strings to check of a given
sentence is a palindrome.
Change all the letters into lower case and remove the spaces '''


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1: -1])
    return isPal(toChars(s))


print(isPalindrome("are"))
print(isPalindrome("fear of oraef"))

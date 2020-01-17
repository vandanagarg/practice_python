#print double characters of the string

a = 'ABC'

def double_char(a):
    to_return = ''
    for c in a:
        to_return += c*2
    # print(to_return)
    return to_return

# double_char("ABC")
print(double_char("ABC"))

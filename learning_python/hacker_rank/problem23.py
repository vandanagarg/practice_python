''' Given an integer, print the following values
for each integer:
Decimal
Octal
Hexadecimal (capitalized)
Binary
'''

n = int(input())
width = len("{0:b}".format(n))
for i in range(1, n+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
        i, width=width))

# 2nd option
STDIN = 17
# print(bin(STDIN))
w = len(str(bin(STDIN)).replace('0b', ''))
# print(oct(int(STDIN)))
# print(oct(int(STDIN)).replace('0','', 1))

for i in range(1, STDIN+1):
    j = str(i).rjust(w, ' ')
    o = oct(int(i)).replace('0o', '', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x', '').upper().rjust(w, ' ')
    b = bin(int(i)).replace('0b', '').rjust(w, ' ')
    print(j, o, h, b)

''' alphabet rangoli of size N '''
import string


alpha = string.ascii_lowercase
# print(alpha)

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    # print(L)
print('\n'.join(L[:0:-1]+L))

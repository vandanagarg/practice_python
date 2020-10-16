''' Capitalize first and only alphabet letter '''


s = "abgs hajs"
# s = "12abgs hajs"
# print(s.capitalize())

# print(s[:].split())

for x in s[:].split():
    # print(x)
    s = s.replace(x, x.capitalize())
print(s)

# o/p: Abgs Hajs
# 12abgs Hajs

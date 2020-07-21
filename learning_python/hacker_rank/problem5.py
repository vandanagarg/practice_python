# converting list into a string


l = [1, 2, 3]

row_string = ""
for i in l:
    row_string = row_string + str(i) + " "
    # print(str(i))
print(row_string)
print(type(row_string))

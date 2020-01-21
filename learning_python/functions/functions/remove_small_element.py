def remove_small_element():
    num = 6
    num_list = [5,89,56,4,8,2,4,1,100]
    new_list = []

    for i in range(0, len(num_list)):
        if num_list[i] > int(num):
            new_list.append(num_list[i])
            #print(num_list[i])

    return new_list

print(remove_small_element())


# list_ex = [56,8,5,8,114,158,2,1]
#
# print(list_ex.pop(0))
# print(list_ex)

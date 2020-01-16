# inp_array = [1,1,2,1,2,1,2,1]
# index_array = [0,5]
# # value = 1
# inp_array = ['*','*','*','0','*','*','0','0','0']
# index_array = [0,1,2]
# element = '*'
#
# def value_in_array(index_array, inp_array,value):
#     all_index_values_matched = True
#     for index in range(0,len(index_array)):
#        index_value = index_array[index]
#        #print(index_value)
#        inp_array_value = inp_array[index_value]
#        #print(inp_array_value)
#        if inp_array_value == value:
#            continue
#        else:
#            all_index_values_matched = False
#            print(all_index_values_matched)
#     return all_index_values_matched

# print(value_in_array(index_array,inp_array,element))


# print(True == True)
# print(True)
#
# print(True == False)
# print(False)

#
# inp_array = [11,2,3,4,8,17]
# num= 3
#
# def slice_from_element(inp_array, num):
#     output_array= []
#     for index in range(0,len(inp_array)):
#         # print(inp_array[index])
#         if inp_array[index] != num:
#             continue
#         else:
#             index_val = index + 1
#             for new_index in range(index_val, len(inp_array)):
#                 output_array.append(inp_array[new_index])
#             return output_array
#             #return  inp_array[index_val:]
#
#
# print(slice_from_element(inp_array,num))



# inp_array = [11,2,3,4,8,17]
# num= 3
#
# def slice_from_element(inp_array, num):
#     value_matched = False
#     output_array= []
#     for index in range(0,len(inp_array)):
#         # print(inp_array[index])
#         if (inp_array[index] != num and value_matched== False):
#             continue
#         elif inp_array[index] == num:
#             value_matched = True
#
#         elif value_matched== True:
#             output_array.append(inp_array[index])
#     return output_array
#             #return  inp_array[index_val:]
#
#
# print(slice_from_element(inp_array,num))



# inp_array = [10, 9 , 8 , 7, 3,2,-1 , 24 , 39, 93]

# print(min(inp_array))
# print(max(inp_array))
#
# def min_value(inp_array):
#     minimum_value = inp_array[0]
#     for value in range(1, len(inp_array)):
#         if minimum_value > inp_array[value]:
#             minimum_value = inp_array[value]
#         else:
#             continue
#     return minimum_value
#
# print(min_value(inp_array))

# C:\Users\as\PycharmProjects\Giraffe\tictactoenew.py










inp_array = [10, 9 , 8 , 7, 3,2,-1 , 24 , 39]

def max_value(inp_array):
    maximum_value = inp_array[0]
    for index in range(1, len(inp_array)):
        if maximum_value < inp_array[index]:
            maximum_value = inp_array[index]
        else:
            continue
    return maximum_value

print(max_value(inp_array))
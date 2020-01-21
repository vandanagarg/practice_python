#Q4: return a unique list:

inp_list = [2,5,2,5,2,5,6,8,6,8,7,9,9,2,1,0]
unique_lst = []

def unique_list(inp_list):
    for item in inp_list:
        if item in unique_lst:
            continue
        else:
            unique_lst.append(item)
    return unique_lst


print(unique_list(inp_list))


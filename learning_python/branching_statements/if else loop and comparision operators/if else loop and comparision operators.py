# if statement and Comparisons  # we can compare number , boolean , strings anything

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:  # its either true or false its not a number just a boolean true or false
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(400, 5, 30))

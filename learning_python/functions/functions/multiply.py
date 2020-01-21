#Q5:  multiply all numbers in a list

numbers = [2,5,8,4]

def multiply(numbers):
    mul_result = 1
    for item in range(0, len(numbers)):
        mul_result = mul_result * int(numbers[item])
    return mul_result


print(multiply(numbers))


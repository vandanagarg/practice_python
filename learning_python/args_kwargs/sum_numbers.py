#example *args

def sum_numbers(*args):
    total = 0
    for nums in args:
        total = total + nums
    return total

print(sum_numbers(5,6,5,8,52,2))

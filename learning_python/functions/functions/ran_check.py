#Q2:  number in range

def ran_check(num, low, high):
    return high >= num >= low

def ran_check(num, low, high):
    if high >= num >= low:
        return "The given number is within the range."
    else:
        return "The given number is not within the range."

print(ran_check(5,2,9))
print(ran_check(8,2,7))
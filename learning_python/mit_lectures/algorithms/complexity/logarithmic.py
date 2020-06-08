''' Examples - Logarithmic Complexity '''


# example1
def int_to_str(i):
    digits = '0123456789'
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

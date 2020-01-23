import pdb


def dectobincalc():
    selector = input("Plaese choose binary_calc or decimal_calc")
    if selector == "binary_calc":
        dec_num = input("Please enter a decimal number.")
        print(dectobin(dec_num))
    elif selector == "decimal_calc":
        bintodec()
    else:
        print("Enter a valid operation")

#1st way:


def dectobin(dec_num, binary_num = []):
    decimal_num = int(dec_num)
    if decimal_num > 1:
        # pdb.set_trace()
        dectobin(decimal_num/2, binary_num)
        # pdb.set_trace()
    binary_num.append(str(decimal_num%2))
    return int(("").join(binary_num))
    # return binary_num


#2nd way:


def dectobin_loop(dec_num):
    n = int(dec_num)
    rem = ""
    while n >= 1:
        rem = rem + (str(n % 2))
        n = n // 2  # n = 2
    print(rem[::-1])


print(dectobin(5))
dectobin_loop(5)


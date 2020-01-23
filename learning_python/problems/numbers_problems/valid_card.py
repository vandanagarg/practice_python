#Problem 13
#Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer)
# and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

# cc = str(raw_input("Enter a credit card number to validate (Mastercard, Visa, Discover, Amex only): "))
#
#
# def val_cc(number):
#     cc_rev = number[::-1]
#     total = 0
#     for i in cc_rev[1::2]:
#         x = int(i) * 2
#         if len(str(x)) == 2:
#             for a in str(x):
#                 total += int(a)
#         else:
#             total += int(x)
#
#     for i in cc_rev[::2]:
#         total += int(i)
#
#     return total
#
#
# if (int(cc[:2]) >= 51 and int(cc[:2]) <= 55 and len(cc) == 16) or \
#         (int(cc[0]) == 4 and (len(cc) == 13 or len(cc) == 16)) or \
#         ((int(cc[:2]) == 34 or int(cc[:2]) == 37) and len(cc) == 15) or \
#         (int(cc[:4]) == 6011 and len(cc) == 16):
#     if val_cc(cc) % 10 == 0:
#         print
#         "%s is a valid credit card number" % cc
#     else:
#         print
#         "%s is NOT a valid credit card number" % cc
# else:
#     print
#     "%s is NOT a valid credit card number" % cc


def validate(n):
    intArray = intToArray(n)

    if len(intArray) % 2 == 0:
        oddEven(0, intArray)
    else:
        oddEven(1, intArray)

    if sum(intArray) % 10 == 0:
        return True
    else:
        return False


def intToArray(n):
    myArray = str(n)

    intArray = []
    for x in myArray:
        intArray.append(int(x))

    return intArray


# Doubles and sums array values
# Odd numbers have startIndex 1
def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 10:
            intArray[i] = newDigit
        else:
            intArray[i] = sumOfDigits(newDigit)


def sumOfDigits(n):
    return (n / 10) + (n % 10)


print(validate(input("Enter CC number to validate\r\n>")))




#Problem 8
#Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

# def converter(num):
#     dec()

# print(hex())
# print(bin())
# print(int("100",2))


def binTodecCalc():
    selection= input("Choose bin_to_dec_calc or dec_to_bin_calc")
    if selection =="bin_to_dec_calc":
        binary = input("Enter a binary number. ")
        binaryTodecimal(binary)

    elif selection =="dec_to_bin_calc":
        decimal = input("Enter a decimal number. ")
        decimalTobinary(decimal)


def binaryTodecimal(binary):
    binary1 = int(binary)
    decimal, i = 0, 0
    while binary1 != 0:
        dec = binary1 % 10
        decimal = decimal + dec * pow(2, i)
        binary1 = binary1 // 10
        i += 1
    print(decimal)


def decimalTobinary(decimal):
    n = int(decimal)
    if (n > 1):
        # divide with integral result
        # (discard remainder)
        decimalTobinary(n // 2)
    print(n % 2, end=' ')

binTodecCalc()

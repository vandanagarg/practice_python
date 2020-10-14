# sWAP cASE


def swap_case(s):
    return s.swapcase()


def swap_case2(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    print(result)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


print(''.join([i.lower() if i.isupper() else i.upper() for i in input()]))

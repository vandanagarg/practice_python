import string


def check_letters(inp_str):
    alphabet = string.ascii_lowercase
    missing_letters = []
    for letter in alphabet:
        if letter in inp_str:
            continue
        else:
            missing_letters.append(letter)
    return missing_letters


print(check_letters("he quick brown fox jumps  t lazy dog"))


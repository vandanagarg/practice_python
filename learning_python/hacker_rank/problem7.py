# Sorting


a = "appleBOY5768"
lower_letters = []
upper_letters = []
even_digits = []
odd_digits = []
for i in a:
    if i.isdigit():
        if int(i) % 2 == 0:
            even_digits.append(i)
        else:
            odd_digits.append(i)
    elif i.islower():
        lower_letters.append(i)
    elif i.isupper():
        upper_letters.append(i)
# print(sorted(a))
print(lower_letters, upper_letters, even_digits, odd_digits)
print(sorted(lower_letters), sorted(upper_letters),
      sorted(even_digits), sorted(odd_digits))
joined_list = sorted(lower_letters) + sorted(
              upper_letters) + sorted(odd_digits) + sorted(even_digits)
print(joined_list)
print("".join(joined_list))

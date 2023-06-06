""" Creating a primitive bar chart """

numbers = [19, 3, 15, 7, 11]

print('\nCREATING A BAR CHART FROM NUMBERS:\n')
print(f'Index{"Value":>8}{"Bar":>6}')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

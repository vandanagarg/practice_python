# enumerate function is used for unpacking sequences, it generates the sequence of tuples
# each tuple contains 2 elements index and the corresponding element

#  example 1

word = 'abcde'

for item in enumerate(word):
    print(item) # generating tuple
    print(type(item))

#  printing only item values at index position 1 
for item in enumerate(word):
    print(item[1])


#  example 2

colors = ['red', 'orange', 'yellow']

print(list(enumerate(colors)))

print(tuple(enumerate(colors)))


# Unpacking Sequences

print(f'unpacking the sequence')

for index, value in enumerate(colors):
    print(f'{index}: {value}')

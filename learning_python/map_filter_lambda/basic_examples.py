#examples

square = lambda num: num ** 2
print(square(5))

my_nums = [10, 20, 30, 45]
print(list(map(lambda num: num ** 2 ,my_nums)))

print(list(filter(lambda num : num% 2 == 0, my_nums)))  #filters based on the matching conditions

names = ['Andy', 'vandana garg', 'Eve', 'Sally']

print(list(map(lambda name: name[:: -1],names)))

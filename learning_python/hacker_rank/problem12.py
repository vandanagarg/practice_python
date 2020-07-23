# OrderedDict
from collections import OrderedDict


n = int(input())
ordered_dictionary = OrderedDict()
for _ in range(n):
    # x, y = map(input().split())
    item, space, quantity = input().rpartition(' ')
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(quantity)
print(ordered_dictionary)

# from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

import collections

list1 = [22,37,54,79,110,500,1700,1720]

list1 = [110,500,1700,1720,22,37,54,79]

for i in range(1,len(list1)):
    if list1[i-1] > list1[i]:
        print(list1[i:] + list1[:i])


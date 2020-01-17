#Count letters in the given string and store the counts as dictionary

a = 'aabbccdddeeepppsssvvvvggggllllll'
d = {}

for letter in a:
    #d_items = d.keys()
    #print([0][0])
    #print(letter)
    if letter in d.keys():
        d[letter] += 1
    else:
        d[letter] = 1
print(d)


#for loop
# special kind of loop as it helps us to loop over a different collections of items

#with strings
for letter in "Giraffe Academy ":
    print(letter)

#with array
freinds = ["Jim", "Karen", "Kevin"]
for freind in freinds:
    print(freind)

#with numbers
for index in range(10):  #o/p will be from 0 to 9 vertically
    print(index)


for index in range(3,10):  #o/p will be from 3 to 9 vertically
    print(index)


for index in range(len(freinds)):
    print(index)            #o/p will be index of array i.e: 0 1 2 vertically
    print(freinds[index])   #o/p will be name of freinds array vertically


for index in range(5):  
    if index == 0:
        print("First iteration !")
    else:
        print("Not first")

#Lists ,we have to use [] these brackets to store a bunch of values and thus we create a list of some related data that we wish to have
#We can put anything in a list i.e: a number, boolean or a string #list is mutable

friends = [ "Peeyush Singla", "PS", "groom", "VG"]
friends_two = [ "Peeyush Singla", "PS", "groom", "VG"]
print(friends) # o/p is as list  # ['Peeyush Singla', 'PS', 'groom', 'VG']
print("My friends are: " + str(friends))  # it prints the whole list # o/p as string : My friends are: ['Peeyush Singla', 'PS', 'groom', 'VG']

# to print a particular value we have to do that by identifying it from their index(starts from 0)
print(friends[0])  # prints first value
print(friends[-2])  # prints second value from the last (so basically negative index is the values from last and it starts from -1 itself)

# to grab a selective inputs #1. lets say from 2nd till last we want to o/p  2. we want to select 2nd and 3rd value
print(friends[1:])  # from 2nd value till end
print(friends[1:3])  # it will print from index value 1 to 2 and will not inclue 3 , thus will just output 2nd nd 3rd value

#to modify any value at a specific location # lets say at 2nd value i want to change from PS to husband
friends[1] = "Husband"
print(friends[1])

##list functions

lucky_numbers = [4, 8 , 15, 16, 23, 42]
friends = [ "Peeyush Singla", "PS", "groom", "VG", "Husband"]

#to append a list use function extend

friends.extend(lucky_numbers)
print(friends)  # it adds all values of lucky_numbers list in list friends at the end

#add individual elements # append function  allows us only to add anything at the end of the list
friends.append("Jaana")
print(friends)

#in order to add any value in between the existing list at some random/ DEFINED place use insert function(will take 2 parameters : value and index value where we wish to insert)
friends.insert(1, "Jaana") #thus inserts Jaana at 1st index place and rest all values are pushed off to the right
print(friends)

#to remove elements #use remove function and pass the value u wish to remove
friends.remove("VG")
print(friends)

friends_two.clear() # to remove all elements or clear the list we use clear function
print(friends_two) # o/p is []

friends.pop() # it basically pops /removes last element from the list
print(friends)

#to see if a value is present in the list , below code will return the index number of the value
print(friends.index("VG"))

#count the similar number of elements in the list
print(friends.count("VG"))

#sort ascending
friends.sort()
print(friends)

#to reverse the order (its not in descending order), it just prints all opposite like back to front it prints
print(friends)
friends.reverse()
print(friends)

#to make a copy of existing list
friends2= friends.copy()
print(" friends2 = " + str(friends2) )

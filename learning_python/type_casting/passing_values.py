#variables and passing values and printing them 
character_name= "mike"
character_age = 50
print("the men " + character_name + ",")
# print( character_age + "years old")  #this wont work see next line of code for typecasting
print( str(character_age) + "years old")
print("liked name " + character_name + ",")
# print("didn't like being " + character_age + "years.")  #this wont work see next sheet of code for typecasting
print("didn't like being " + str(character_age) + "years.")

#strings and index values
phrase = "Giraffe Acedamy"
print(phrase[0])
# print(phrase.index("z"))  #gives error since its not present

#replacing a value in a string
print(phrase.replace("a","Elephant"))

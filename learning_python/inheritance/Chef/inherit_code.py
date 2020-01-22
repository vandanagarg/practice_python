#Inheritance  # we can define a class and define some attributes and functions in the class and then use this class in some other class

from Chef import Chef

myChef = Chef()
myChef.make_chicken()

#now if we want to make a class that model a different type of chef
#lets see our Chinese Chef

from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()


from ChineseChef import ChineseChef_import

myChineseChef = ChineseChef_import()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()


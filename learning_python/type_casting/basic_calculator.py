#Building a basic calculator
num1 = input("Enter a number : ")  # lets say 12
num2 = input("Enter another number : ")   #lets say 2

result = num1 + num2
print("the sum of numbers is : " + result)  # with this line of code input would be treated as a string and thus result would be a string
#o/p is the sum of numbers is : 122

#to treat input as int (where numbers can be just whole numbers) or float (where we can use decimal numbers as well) use type casting as below

result = int(num1) + int(num2)
print("the sum of numbers is : " + str(result))  #now answer is the sum of numbers is : 14
print(result)  # 14

#for decimal inputs #lets say 12.6 and 2.8
result = float(num1) + float(num2)
print("the sum of numbers is : " + str(result))  #now answer is the sum of numbers is : 15.399999999999999
print(result)  # 15.399999999999999


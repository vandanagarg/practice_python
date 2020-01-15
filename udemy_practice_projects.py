import pdb

# Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

# def return_pie(n = 15):
#     result = float(22/7)
#     return round(result,n)
# #
# print(return_pie(50))

# print((4/1) - (4/3)+ (4/5) - (4/7) + (4/9) - (4/11) + (4/13)- (4/15) + (4/17)- (4/19) + (4/21)- (4/23) + (4/25)- (4/27) + (4/29)- (4/31) + (4/33))

# def cal_pie(limit):
#     num = 4
#     result = 0
#     cycle_start = True
#
#     # if limit > 15:
#     #     print("LIMIT can't be greater than 15.")
#     #     limit = 15
#
#     for denom in range(1, 10^limit, 2):
#         # print(limit)
#         if cycle_start:
#             result = result + (num / denom)
#         else:
#             result = result - (num / denom)
#
#         cycle_start = not cycle_start
#     return round(result, limit)
#
#
# print(cal_pie(100000000000))


#problem 2
#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

# def fib(num):
#     a = 0
#     b = 1
#     for n in range(num):
#         yield a
#         a, b = b, a+b
#
# print(list(fib(10)))
#
# for x in fib(10):
#     print(x)


#problem 3
#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             # n //= i
#             n = n/i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
# print(prime_factors(15))

# def find_prime_fac(n):
#     list_of_factors=[1]
#     unique_list_factors = []
#     i= 2
#     while n > 1:
#         if n % i == 0:
#             list_of_factors.append(i)
#             n = n / i
#             i = i - 1
#         i += 1
#
#     for l in list_of_factors:
#         if l not in unique_list_factors:
#             unique_list_factors.append(l)
#
#     return unique_list_factors
#
# print(find_prime_fac(146))

# #problem 4
# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
#
# choice = input("Continue finding prime numbers (y/n)? ")
# current = 1
#
# def is_prime(n):
#     # print("n is :" + str(n))
#     # print(current)
#     if n % 2 == 0:
#         return False
#
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#
#     return True
#
# while choice.lower().startswith('y'):
#     current += 1
#     # print("current in while is: " + str(current))
#     while is_prime(current) == False:
#         current += 1
#
#     print("Next prime is: " + str(current))
#     choice = input("Continue finding prime numbers (y/n)? ")
#

####################################################################################
# def print_prime_num(prime_number):
#     print("Prime number is: " + str(prime_number))
#
# def next_prime_num():
#     prime_number = 1
#     print_prime_num(prime_number)
#     while (input("Do you want to see next prime number? Yes or No") == "Yes" ):
#         prime_number = get_prime_num(prime_number)
#         print_prime_num(prime_number)
#
# def get_prime_num(previous_prime_number):
#     n = previous_prime_number + 1
#     i = 2
#     if n == 2:
#         return n
#     else:
#         while i < n:
#             if n % i == 0:
#                 # n += 1
#                 n = get_prime_num(n)
#                 # break
#             elif n % i != 0:
#                 i += 1
#         return n
#
#
# # next_prime_num()
# ####################################################################################
# def print_prime_num(prime_number):
#     print("Prime number is: " + str(prime_number))
#
# def next_prime_num():
#     prime_number = 1
#     print_prime_num(prime_number)
#     while (input("Do you want to see next prime number? Yes or No") == "Yes" ):
#         prime_number = check_next_prime_num(prime_number)
#         # print_prime_num(prime_number)
#
# def check_next_prime_num(prime_number):
#     next_prime_num = prime_number + 1
#     # is_prime = prime_num(next_prime_num)
#     prime = prime_num(next_prime_num)
#     print(prime)
#     # if is_prime:
#     #     print_prime_num(next_prime_num)
#     #     return next_prime_num
#     # else:
#     #     next_prime_num = prime_num(n)
#     #     print(next_prime_num)
#     #     return next_prime_num
#
#     #     next_prime_num += 1
#     #     prime_num(next_prime_num)
#     #     return next_prime_num
#
#
# def prime_num(n):
#     count = 0
#     for i in range(1,n):
#         if n%i == 0:
#             count +=1
#     if n==1 or count == 1:
#         return n
#     else:
#         n += 1
#         # print(n)
#         prime_num(n)
#         while prime_num(n):
#             return n
#
#
#
# # next_prime_num()
#
#
# ###############################################
#
#
# # def prime_num(n):
# #     count = 0
# #     for i in range(1,n):
# #         if n%i == 0:
# #             count +=1
# #     if n==1 or count == 1:
# #         print("Entered number is prime")
# #     else:
# #         print("Entered number is not prime")
# #
# # # prime_num(1)
#
#
#
# ######################################################
#
#
# def print_next_ten_num(num):
#     for i in range(1,11):
#         print(num + i)
#
# # print_next_ten_num(2)
#
#
# def is_even(num):
#     return num % 2 == 0
#
# # print(is_even(14))
#
# def check_even():
#     for i in range(1,11):
#         if is_even(i):
#             print(str(i) +" is even number.")
#         else:
#             print(str(i)+ " is odd number.")
#
# # check_even()
#
# def get_ten_even(num):
#     even_list=[]
#     i = num
#     while i <= num+10:
#
#         if is_even(i):
#             even_list.append(i)
#         i += 1
#     return even_list
#
# # print(get_ten_even(5))
#
# # i = 1
# # while i <= 10:
# #     print(i)
# #     i+=1
#
#
# def get_ten_even2(num):
#     even_list= []
#     for i in range(num, num+10):
#         if is_even(i):
#             even_list.append(i)
#     return even_list
#
# # print(get_ten_even2(5))
#
# def next_even_num(num):
#     i =  num + 1
#     while True:
#         if is_even(i):
#             return i
#         else:
#             i +=1
#
# # print(next_even_num(1))
# # print(next_even_num(2))
#
#
# ###########################################
#
# def is_prime(num):
#     count = 0
#     for i in range(1,num):
#         if num%i == 0:
#             count+=1
#
#     return num == 1 or count ==1
#
# def next_prime(number):
#     i = number +1
#     while True:
#         if is_prime(i):
#             return "prime num is: "+ str(i)
#         else:
#             i += 1
#
# # print(next_prime(4))
# # print(next_prime(5))
# print(next_prime(11))
# print(next_prime(13))



########################
# Problem 5
#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

# def area_floor(width =1 , height = 1):
#     return float(width * height)
#
# def cost(amount):
#     return float(area_floor() * amount)
#
# print(cost(4))


################
#Problem 6
#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan. For added complexity,
# add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# def mortgage_calculator():
#     months = int(input("Enter mortgage term (in months): "))
#     rate = float(input("Enter interest rate: "))
#     loan = float(input("Enter loan value: "))
#
#     monthly_rate = rate / 100 / 12
#     payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
#
#     return payment
#
# print(mortgage_calculator())


############
#Problem 7
#Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change

# def purchase():
#     purchamt=float(input("Enter the cost of the item purchased: "))
#     payamt=float(input("Enter the amount paid for the item: "))
#     change, dollars, quarters, dimes, nickels, pennies = calc_change(purchamt, payamt)
#     printresults(change, dollars, quarters, dimes, nickels, pennies)
#
# # pdb.set_trace()
#
# def calc_change(purchamt, payamt):
#     change = payamt - purchamt
#     cents = change*100+0.01
#     print(cents)
#     dollar_amount = int(cents /100)
#     dollars = dollar_calc(dollar_amount)
#     cents = cents %100
#     quarters = int(cents/25)
#     cents = cents %25
#     dimes = int(cents/10)
#     cents = cents %10
#     nickels = int(cents/5)
#     cents = cents %5
#     pennies = int(cents)
#     return change, dollars, quarters, dimes, nickels, pennies
#
# def dollar_calc(dollar_amount):
#     change_of_100 = int(dollar_amount/100)
#     dollar_amount = dollar_amount%100
#     change_of_50 = int(dollar_amount/50)
#     dollar_amount = dollar_amount % 50
#     change_of_10 = int(dollar_amount / 10)
#     dollar_amount = dollar_amount % 10
#     change_of_2 = int(dollar_amount / 2)
#     dollar_amount = dollar_amount % 2
#     change_of_1 = int(dollar_amount / 1)
#     dollar_amount = dollar_amount % 1
#     return (str(change_of_100)+ " of 100" ,str(change_of_50)+ "  of 50",str(change_of_10)+ " of 10",str(change_of_2)+ " of 2",str(change_of_1)+ " of 1" )
#
# def printresults(change, dollars, quarters, dimes, nickels, pennies):
#     print("Amount of change to give back: ", change)
#     print('dollars: $', dollars)
#     print('quarters: ', quarters)
#     print('dimes: ', dimes)
#     print('nickels: ', nickels)
#     print('pennies: ', pennies)
#     return
#
# purchase()



###########
#Problem 8
#Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

# def converter(num):
#     dec()

# print(hex())
# print(bin())
# print(int("100",2))

#
# def binTodecCalc():
#     selection= input("Choose bin_to_dec_calc or dec_to_bin_calc")
#     if selection =="bin_to_dec_calc":
#         binary = input("Enter a binary number. ")
#         binaryTodecimal(binary)
#
#     elif selection =="dec_to_bin_calc":
#         decimal = input("Enter a decimal number. ")
#         decimalTobinary(decimal)
#
#
# def binaryTodecimal(binary):
#     binary1 = int(binary)
#     decimal, i = 0, 0
#     while binary1 != 0:
#         dec = binary1 % 10
#         decimal = decimal + dec * pow(2, i)
#         binary1 = binary1 // 10
#         i += 1
#     print(decimal)
#
#
# def decimalTobinary(decimal):
#     n = int(decimal)
#     if (n > 1):
#         # divide with integral result
#         # (discard remainder)
#         decimalTobinary(n // 2)
#     print(n % 2, end=' ')
#
# binTodecCalc()

#######################################

# import pdb
#
#
# def dectobincalc():
#     selector = input("Plaese choose binary_calc or decimal_calc")
#     if selector == "binary_calc":
#         dec_num = input("Please enter a decimal number.")
#         print(dectobin(dec_num))
#     elif selector == "decimal_calc":
#         bintodec()
#     else:
#         print("Enter a valid operation")


# def dectobin(dec_num, binary_num = []):
#     decimal_num = int(dec_num)
#     if decimal_num > 1:
#         # pdb.set_trace()
#         dectobin(decimal_num/2, binary_num)
#         # pdb.set_trace()
#     binary_num.append(str(decimal_num%2))
#     return int(("").join(binary_num))
# return binary_num

# def dectobin(dec_num):
#     n = int(dec_num)
#     rem = ""
#     while n >= 1:
#         rem = rem + (str(n % 2))
#         n = n // 2  # n = 2
#     print(rem[::-1])


# int number
# divide it by 2 till number becoomes 1
# return remainder for each run 1,0


# dectobin(8)


# def bintodec():
#     pass
#
#
# # dectobincalc()
# # dectobin(5)
#

#############
#Problem 9
# Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.


# def add(x, y):
#    return x + y
#
# # This function subtracts two numbers
# def subtract(x, y):
#    return x - y
#
# # This function multiplies two numbers
# def multiply(x, y):
#    return x * y
#
# # This function divides two numbers
# def divide(x, y):
#    return x / y
#
#
# def calc():
#     print("Select operation.")
#     print("1.Add")
#     print("2.Subtract")
#     print("3.Multiply")
#     print("4.Divide")
#
#     choice = input("Enter choice(1/2/3/4): ")
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if choice == '1':
#         print(num1,"+",num2,"=", add(num1,num2))
#     elif choice == '2':
#         print(num1,"-",num2,"=", subtract(num1,num2))
#     elif choice == '3':
#         print(num1,"*",num2,"=", multiply(num1,num2))
#     elif choice == '4':
#         print(num1,"/",num2,"=", divide(num1,num2))
#     else:
#         print("Invalid input")
#
# calc()


# Calculator
# Have the user enter 2 number - a. b -
# and an operator - op - and calculate
# the solution - c - according to the
# type of the given operator


# def calc(a, b, op):
#     """
#     Returns a string like this: a op b = c
#     where c is the computed value according to the opeartor
#     """
#
#     if op not in '+-/*':
#         return 'Please only type one of these characters: "+, -, *, /"!'
#
#     if op == '+':
#         return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
#     if op == '-':
#         return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
#     if op == '*':
#         return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
#     if op == '/':
#         return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))
#
#
# def main():  # Wrapper function
#
#     a = int(input('Please type the first number: '))
#     b = int(input('Please type the second number: '))
#     op = input(
#         'What kind of operation would you like to do?\
#         \nChoose between "+, -, *, /" : ')
#
#     print(calc(a, b, op))
#
# if __name__ == '__main__':
#     main()
#


################
#Problem 10
#Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another.
# The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
# The program will then make the conversion.

# from math import ceil
# import urllib.request
# import json
#
#
# class Converter():
#     _temps = {'cf': lambda c: c * (9 / 5) + 32,
#               'fc': lambda f: (f - 32) * (5 / 9),
#               'ck': lambda c: c + 273.15,
#               'kc': lambda k: k - 273.15,
#               'fk': lambda f: (f + 459.67) * 5 / 9,
#               'kf': lambda k: k * (9 / 5) - 459.67
#               }
#
#     @classmethod
#     def binToDec(cls, bin_no):
#         """
#         @param bin_no:  an integer or str representation of a binary number
#         @return:        an integer value of the binary number passed
#         """
#         dec = 0
#         i = 0
#         if not isinstance(bin_no, int):
#             try:
#                 bin_no = int(bin_no)
#             except:
#                 raise TypeError
#         while bin_no > 0:
#             dec += ((bin_no % 10) * (2 ** i))
#             bin_no //= 10
#             i += 1
#         return dec
#
#     @classmethod
#     def decToBin(cls, dec_no, bit_rep):
#         """
#         @param dec_no:  an integer value
#         @param bit_rep: bit representation amount
#         @return:        a string representation of the decimal value passed
#         """
#         if dec_no > 0:
#             return str(bin(dec_no)[2:].zfill(bit_rep))
#         return '-' + str(bin(dec_no))[2:].zfill(bit_rep)
#
#     @classmethod
#     def currencyExchange(cls, con_from, con_to, value):
#         """
#         @param con_from:a string representation of the currency to convert from
#         @param con_to:  a string representation of the currency to convert to
#         @param value:   amount to convert
#         @return:        the value of the conversion from con_from to con_to of value
#         """
#         result = 0
#         curr_page = urllib.request.urlopen(
#             'http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
#         obj = curr_page.read().decode(encoding='UTF-8')
#         content = json.loads(obj)
#         try:
#             _from = content['rates'][con_from]
#             _to = content['rates'][con_to]
#             convert_amt = _to / _from
#             result = convert_amt * value
#         except:
#             raise NameError
#         return result
#
#     @classmethod
#     def tempConvert(cls, msr_from, msr_to, amt):
#         """
#         @todo:    Rounding... /sigh
#         @param msr_from:a string representation of the measurement to convert from
#         @param msr_to:  a string representation of the measurement to convert to
#         @param amt:     the value to convert
#         @return:        the converted temperature value
#         """
#         try:
#             return cls._temps[msr_from[0] + msr_to[0]](amt)
#         except KeyError:
#             "Cannot convert from {0} to {1}".format(msr_from, msr_to)
#
#     pass
#



################
#Problem 11
#Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
# import time
#
# def alarm(n):
#     print("Wait time:", n, "seconds.")
#     time.sleep(n)  # Waits 'n' seconds before playing sound
#     print("Time over")
#
#
# def input_destinations(user_input):
#     if user_input == '1':
#
#         user_input = int(input("Enter the desired hours: "))
#
#         wait_time = (user_input * 60) * 60
#         alarm(wait_time)
#
#     elif user_input == '2':
#
#         user_input = int(input("Enter the desired minutes: "))
#
#         wait_time = user_input * 60
#         alarm(wait_time)
#
#     elif user_input == '3':
#
#         user_input = int(input("Enter the desired seconds: "))
#
#         wait_time = user_input
#         alarm(wait_time)
#
#     elif user_input == '4':
#
#         hours = int(input("Hours: "))
#         minutes = int(input("Minutes: "))
#         seconds = int(input("Seconds: "))
#
#         wait_time = ((hours * 60) * 60) + (minutes * 60) + seconds
#         print(wait_time)
#         alarm(wait_time)

#
# def main():
#     print("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
#     main_input = input(": ")
#
#     input_destinations(main_input)
#
#     return
#
#
# main()
#



################
#Problem 12
# Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance.
# This program may require finding coordinates for the cities like latitude and longitude.

# import math
#
# def distance(origin, destination):
#     lat1, lon1 = origin
#     lat2, lon2 = destination
#     radius = 6371 # km
#
#     dlat = math.radians(lat2-lat1)
#     dlon = math.radians(lon2-lon1)
#     a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
#         * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#     d = radius * c
#
#     return d
#
#
# print(distance((100,2000),(545,2365)))



################
#Problem 13
#Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer)
# and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

# cc = str(raw_input("Enter a credit card number to validate (Mastercard, Visa, Discover, Amex only): "))
#
#
# def val_cc(number):
#     cc_rev = number[::-1]
#     total = 0
#     for i in cc_rev[1::2]:
#         x = int(i) * 2
#         if len(str(x)) == 2:
#             for a in str(x):
#                 total += int(a)
#         else:
#             total += int(x)
#
#     for i in cc_rev[::2]:
#         total += int(i)
#
#     return total
#
#
# if (int(cc[:2]) >= 51 and int(cc[:2]) <= 55 and len(cc) == 16) or \
#         (int(cc[0]) == 4 and (len(cc) == 13 or len(cc) == 16)) or \
#         ((int(cc[:2]) == 34 or int(cc[:2]) == 37) and len(cc) == 15) or \
#         (int(cc[:4]) == 6011 and len(cc) == 16):
#     if val_cc(cc) % 10 == 0:
#         print
#         "%s is a valid credit card number" % cc
#     else:
#         print
#         "%s is NOT a valid credit card number" % cc
# else:
#     print
#     "%s is NOT a valid credit card number" % cc


def validate(n):
    intArray = intToArray(n)

    if len(intArray) % 2 == 0:
        oddEven(0, intArray)
    else:
        oddEven(1, intArray)

    if sum(intArray) % 10 == 0:
        return True
    else:
        return False


def intToArray(n):
    myArray = str(n)

    intArray = []
    for x in myArray:
        intArray.append(int(x))

    return intArray


# Doubles and sums array values
# Odd numbers have startIndex 1
def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 10:
            intArray[i] = newDigit
        else:
            intArray[i] = sumOfDigits(newDigit)


def sumOfDigits(n):
    return (n / 10) + (n % 10)


print
validate(input("Enter CC number to validate\r\n>"))






################
#Problem 14
#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

#Asks the user to enter a cost and either a country or state tax.
#It then returns the tax plus the total cost with tax.

# def rate_cal():
#     cost = input('What is the cost?')
#     rate = input('What is the tax rate? (in %)')
#
#     rate = float(rate) / 100
#     tax = float(rate) * float(cost)
#     total_cost = tax + float(cost)
#
#     print('Tax cost: ' + str(tax))
#     print('Total cost: ' + str(total_cost))
#
# rate_cal()


################
#Problem 15
#Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0,
# is defined as being 1. Solve this using both loops and recursion.

#using loop
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact
#
#
# # print(factorial(4))
#
#using recursion
# def factorial_recursion(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial_recursion(num - 1)
#
#
# print(factorial_recursion(4))



################
#Problem 16
#Complex Number Algebra - Show addition, multiplication, negation, and inversion of complex numbers in separate functions.
# (Subtraction and division operations can be made with pairs of these operations.) Print the results for each operation tested.

from math import sqrt

class complex:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def add(self):
        return number(self.x.r+self.y.r, self.x.im+self.y.im).show()

    def multi(self):
        return number(	self.x.r*self.y.r-self.x.im*self.y.im, self.y.r*self.x.im+self.x.r*self.y.im).show()



class number:
    def __init__(self, x, y):
        self.r = x
        self.im = y

    def show(self):
        print(self.r,self.im)

    def negation(self):
        self.r = self.r*-1
        self.im = self.im*-1
        return self

    def inversion(self):
        root = sqrt(self.r*self.r + self.im*self.im)
        self.r = (self.r/root)
        self.im = -(self.im/root)
        return self


n1 = number(3,2)
n2 = number(1,1)


n1.negation().show()
n1.inversion().show()

c = complex(n1,n2)

c.add()

c.multi()







################
#Problem 17
#Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares
# of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers,
# while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.



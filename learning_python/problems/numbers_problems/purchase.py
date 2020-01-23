#Problem 7
#Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change

import pdb


def purchase():
    purchamt=float(input("Enter the cost of the item purchased: "))
    payamt=float(input("Enter the amount paid for the item: "))
    change, dollars, quarters, dimes, nickels, pennies = calc_change(purchamt, payamt)
    printresults(change, dollars, quarters, dimes, nickels, pennies)

# pdb.set_trace()


def calc_change(purchamt, payamt):
    change = payamt - purchamt
    cents = change*100+0.01
    print(cents)
    dollar_amount = int(cents /100)
    dollars = dollar_calc(dollar_amount)
    cents = cents %100
    quarters = int(cents/25)
    cents = cents %25
    dimes = int(cents/10)
    cents = cents %10
    nickels = int(cents/5)
    cents = cents %5
    pennies = int(cents)
    return change, dollars, quarters, dimes, nickels, pennies


def dollar_calc(dollar_amount):
    change_of_100 = int(dollar_amount/100)
    dollar_amount = dollar_amount%100
    change_of_50 = int(dollar_amount/50)
    dollar_amount = dollar_amount % 50
    change_of_10 = int(dollar_amount / 10)
    dollar_amount = dollar_amount % 10
    change_of_2 = int(dollar_amount / 2)
    dollar_amount = dollar_amount % 2
    change_of_1 = int(dollar_amount / 1)
    dollar_amount = dollar_amount % 1
    return (str(change_of_100)+ " of 100" ,str(change_of_50)+ "  of 50",str(change_of_10)+ " of 10",str(change_of_2)+ " of 2",str(change_of_1)+ " of 1" )


def printresults(change, dollars, quarters, dimes, nickels, pennies):
    print("Amount of change to give back: ", change)
    print('dollars: $', dollars)
    print('quarters: ', quarters)
    print('dimes: ', dimes)
    print('nickels: ', nickels)
    print('pennies: ', pennies)
    return


purchase()


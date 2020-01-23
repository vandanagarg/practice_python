#Problem 14
#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

#Asks the user to enter a cost and either a country or state tax.
#It then returns the tax plus the total cost with tax.


def rate_cal():
    cost = input('What is the cost?')
    rate = input('What is the tax rate? (in %)')

    rate = float(rate) / 100
    tax = float(rate) * float(cost)
    total_cost = tax + float(cost)

    print('Tax cost: ' + str(tax))
    print('Total cost: ' + str(total_cost))


rate_cal()


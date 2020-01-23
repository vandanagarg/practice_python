#Problem 6
#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan. For added complexity,
# add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).


def mortgage_calculator():
    months = int(input("Enter mortgage term (in months): "))
    rate = float(input("Enter interest rate: "))
    loan = float(input("Enter loan value: "))

    monthly_rate = rate / 100 / 12
    payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan

    return payment


print(mortgage_calculator())


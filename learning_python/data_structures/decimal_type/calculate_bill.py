## calculate restaurant bill

from decimal import Decimal

tax = Decimal(6.25)
bill_amount = Decimal(37.45)

total_bill = bill_amount + (bill_amount * (tax/100))
# bill_amount (1 + tax)
print(f'total bill is:{total_bill:>10.2f}')

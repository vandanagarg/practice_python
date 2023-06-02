from decimal import Decimal

principal = Decimal('1000.00')
print("principal: ", principal)

rate = Decimal('0.05')
print("rate: ", rate)
print(type(rate))

x = Decimal('10.5')
y = Decimal('2')

print(f'sum : {x + y}')
print(f'floor division: {x//y}')
print(f'normal division: {x/y}')


num = 1000.00
print(num)
print(f'num is: {num:.20f}')

for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')
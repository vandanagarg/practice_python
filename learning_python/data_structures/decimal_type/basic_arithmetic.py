from decimal import Decimal

principal = Decimal('1000.00')
print(principal)

rate = Decimal('0.05')
print(rate)
print(type(rate))

x = Decimal('10.5')
y = Decimal('2')

print(f'sum : {x + y}')
print(f'floor division: {x//y}')
print(f'normal division: {x/y}')


num = 1000.00
print(num)
print(f'num is: {num:.20f}')

# for 
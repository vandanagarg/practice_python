# generating random numbers by rolling 6 face die

import random


for roll in range(10):  # rolling a die 10 times
    print(random.randrange(1,7), end=' ')  # generating numbers 1 to 6 (6faces of die)

print('\n')

'''  for reproducability/ getting same results everytime use random.seed(_specific_number_)'''

# face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

# 6000000 die rolls
for roll in range(6_000_000): # note underscore seperators
    face = random.randrange(1,7)

    # increment face counter
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1
    
print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')

print('\n')

# getting same output always

# case1
print("case1")
random.seed(32)

for roll in range(10):  # rolling a die 10 times
    print(random.randrange(1,7), end=' ')  # generating numbers 1 to 6 (6faces of die)

print('\n')

# case2
print("case2")

random.seed(35)

for roll in range(10):  # rolling a die 10 times
    print(random.randrange(1,7), end=' ')  # generating numbers 1 to 6 (6faces of die)

print('\n')

# case3
print("case3")

random.seed(32)

for roll in range(10):  # rolling a die 10 times
    print(random.randrange(1,7), end=' ')  # generating numbers 1 to 6 (6faces of die)

# output of case 1 and 3 will always be same.

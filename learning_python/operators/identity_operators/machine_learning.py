import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pd.set_option("max_columns", 50)


#tensor flow ??
#Pandas is built on top of TensorFlow.  no
#ide jupyter notebook

## to see your home directory
# import os
# print(os.path.expanduser('~'))

#C:\Users\as

## Identity operators in Python
#Identity operators compare the memory locations of two objects  - is and is not are 2 identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
# print(x1 is not y1)

# Output: True
# print(x2 is y2)

# Output: False
print(x3 is not y3)
print(id(x3))
print(id(y3))
print(x3 == y3)
print(id(x1))
print(id(y1))
print(id(x2))
print(id(y2))

import math
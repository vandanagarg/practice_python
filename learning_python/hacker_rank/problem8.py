# numpy polynomials, polyval()
import numpy as np


s = list(map(int, input().split()))
print(s)

a = np.polyval([1, 2], 2)
print(a)

poly = list(map(float, input().split()))
x = int(input())

print(np.polyval(poly, x))

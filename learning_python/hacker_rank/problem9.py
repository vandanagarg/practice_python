# numpy: linear algebra: find determinant
# The linalg.det tool computes the determinant of an array.
import numpy


print(round(numpy.linalg.det([[1, 2], [2, 1]]), 2))

# input a  2D array
x = int(input())
in_matrix = []
for i in range(0, x):
    in_matrix.append(list(map(float, input().split())))
print(in_matrix)

print(round(numpy.linalg.det(in_matrix), 2))

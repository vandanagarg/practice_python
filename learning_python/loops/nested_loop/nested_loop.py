#2D lists & nested loops
#creating a 2D structure using lists

number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][1])

#nested for loop:

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)
        
        
#  o/p
#
#   C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# 2
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [0]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
#
# Process finished with exit code 0

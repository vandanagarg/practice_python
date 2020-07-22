# zip() function


print(list(zip([1, 2, 3, 4, 5, 6], 'Hacker')))
print(list(zip([1, 2, 3, 4, 5, 6], 'Hacker')))
# [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]

print(list(zip([1, 2, 3, 4, 5, 6], [0, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
print(list(zip([1, 2, 3, 4, 5, 6], [0, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
# [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]

A = [1, 2, 3]
B = [6, 5, 4]
C = [7, 8, 9]
X = [A] + [B] + [C]

print(list(zip(*X)))
print(list(zip(A, B, C)))
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]


# 5 3
# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5

n, x = (map(int, input().split()))
student_marks = []

for i in range(0, x):
    student_marks.append(list(map(float, input().split())))
print(student_marks)

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i)/len(i))

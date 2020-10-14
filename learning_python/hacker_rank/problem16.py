''' 2nd lowest scores and students '''
students_list = [['Harry', 37.21], ['Berry', 37.21],  ['Tina', 37.2],
                 ['Akriti', 41.0], ['Harsh', 39.0]]
# students_list = [[37.21, 'Harry'], [37.21, 'Berry'], [37.21, 'Tina'],
#                    [36.19, 'Akriti'], [39.0, 'Harsh']]
# students_list = sorted(students_list)
# students_list.remove(min(students_list))
# print(students_list)

# records = []
# for i in range(1, len(students_list)):
#     if students_list[i-1][0] == students_list[i][0]:
#         records.append(students_list[i-1][1])
#         records.append(students_list[i][1])

# records = sorted(set(records))
# print(records)
# for i in records:
#     print(i)

# print(sorted(set([marks for name, marks in students_list])))
print(sorted(set([marks for name, marks in students_list]))[1])

second_highest = sorted((set([marks for name, marks in students_list])))[1]
# print(second_highest)
# print(sorted(students_list))
print('\n'.join([a for a, b in sorted(students_list) if b == second_highest]))

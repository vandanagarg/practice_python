''' 2nd lowest scores and students '''
students_list = [['Harry', 37.21], ['Berry', 37.21],  ['Tina', 37.2],
                 ['Akriti', 41.0], ['Harsh', 39.0]]
# students_list = [[37.21, 'Harry'], [37.21, 'Berry'], [37.2, 'Tina'],
#                    [41.0, 'Akriti'], [39.0, 'Harsh']]
# students_list = sorted(students_list)
# students_list.remove(min(students_list))


second_highest = sorted(list(set([marks for name, marks in students_list])))[1]
print(second_highest)
print('\n'.join([a for a, b in sorted(students_list) if b == second_highest]))

#list with marks of students of eng and maths, add the list using zip and store sum of 2 lists in that.=  ques  to solve

num_maths = [3,32,35,56,6,77,3,13,54,65,67,63]
num_eng =[54,56,45,4,4,5,11,55,1,24,55,11,55,45]
total_marks = []
combine_lists = zip(num_maths,num_eng)
print(combine_lists)

for item in zip(num_maths,num_eng):
    total_marks.append(item[0] + item[1])
   # print (total_marks)

print(total_marks)

#total_marks = num_maths + num_eng
#print(total_marks)

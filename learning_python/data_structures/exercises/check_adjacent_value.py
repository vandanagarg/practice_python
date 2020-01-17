#optimized code
def has_33(nums):
    #print (len(nums))
    
    #for input_num in nums:
    input_num= nums
    
    #print (input_num)
    
    check_true_false = []
    for i in range(1, len(nums)):
        
        #print(i)
        #print(input_num[i])
        #print(input_num[i-1])
        if input_num[i] ==  input_num[i-1] ==3:
            check_true_false.append('True')
        else:
            check_true_false.append('False')
        #print (check_true_false)
        #print (i)
        #i = i+ 1
        #print(i)
    return 'True' in check_true_false
    
    
#     # Check
print(has_33([1, 3, 3]))
# o/p:
# True
#
# # Check
print(has_33([1, 3, 1, 3]))
# o/p:
# False

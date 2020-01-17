#check first and last element of list for equality

a = [1,2,5]
def first_last6 (a):
        #if a[0] or a[len(a) - 1]  == 6:
        if a[0]== 6 or a[- 1]  == 6:
            return True
        else:
            return False

print(first_last6(a))



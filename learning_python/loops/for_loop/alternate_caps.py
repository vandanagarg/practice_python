def myfunc(*args):
    aA =''
    for item in args:
        #print(item)
        for i in range (0, len(item)):
            if i%2 == 0:
                a = item[i].lower()
                #print (a)
            else:
                a = item[i].upper()
                #print (a)
            i = i+ 1
            aA = aA+ a
        return aA
        
        
        
print(myfunc('Peeyush,Vandana'))
# o/p
# 'pEeYuSh,vAnDaNa'
#
print(myfunc('Peeyush'))

# o/p
# 'pEeYuSh'

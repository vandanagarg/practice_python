def alt_caps(args):
    aA =''
    for i in range (0, len(args)):
        if i%2 == 0:
            a = args[i].lower()
            # print(a)
        else:
            a = args[i].upper()
            # print(a)
        i = i+ 1
        aA = aA+ a
    return aA
        
print(alt_caps('ichliebedichmeinehefrau'))

#write a function to capitalize alternate letters of the words entered

#1st way:

def myfunc(args):
    aA =''
    for i in range (0, len(args)):
        if i%2 == 0:
            a = args[i].lower()
        else:
            a = args[i].upper()
        i = i+ 1
        aA = aA+ a
    return aA


print(myfunc('Peeyush'))



# 2nd way - using *args
#single argument

def myfunc(*args):
    for args in args:
        print (args[0])

myfunc('Vandana')

#more than one argument

def myfunc(*args):
    aA =''
    for item in args:
        # print(item)
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


#optimizing the code

def myfunc(*args):
    out_string =''
    for input_string in args:
        #print(input_string)
        for i in range (0, len(input_string)):
            if i%2 == 0:
                a = input_string[i].lower()
                #print (a)
                #i = i+ 1
            else:
                a = input_string[i].upper()
                #print (a)
            #i = i+ 1
            out_string = out_string + a
    return out_string

result= myfunc('Peeyush','vandana')
print(result)

#final optimized code


def formatArrayOfString(*args):
    formatted_strings_array = []
    for input_string in args:
        print(input_string)
        formatted_string = ''
        for i in range(0, len(input_string)):
            if i % 2 == 0:
                formatted_char = input_string[i].lower()
            else:
                formatted_char = input_string[i].upper()
            formatted_string = formatted_string + formatted_char
        formatted_strings_array.append(formatted_string)

    return formatted_strings_array

result = formatArrayOfString('peeyush', 'vandana')
print (result)


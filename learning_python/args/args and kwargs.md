
# Implementation of *args and **kwargs

#Implementation of *args


```python
def myfunc(a,b):  
    #returns the 5% of the sum of a and b
    return sum((a,b)) * 0.05
```


```python
myfunc(40,60)
```

output:

    5.0



now in above the parameters are restricted and are positional arguments but to extend teh limit to take any n number of arguments , we use *args and *kwargs


```python
def myfunc(*args):  #here it will consider all values as a tuple for the number of parameters that are coming in
    return sum(args) * 0.05
```


```python
myfunc(5)
```

output:

    0.25




```python
myfunc(6,4)
```


output:

    0.5




```python
myfunc(8,2,5565,5562,22,12)
```


output:

    558.5500000000001




```python
def myfunc(*spam):  #its an arbitrary keyword not particulary args but * is important but better to use args #returns tuples
    print(spam)
```


```python
myfunc(8+2+5565+5562+22+12)
```

output:

    (11171,)
    


```python
myfunc(8,2,5565,5562,22,12) 
```

output:

    (8, 2, 5565, 5562, 22, 12)
    


#Implementation of **kwargs (**kwargs to return a dictionary)


```python
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}.".format(kwargs['fruit']))
    else:
        print ("There is no fruit of my choice here.")

```


```python
myfunc(fruit = 'apple', veggie = 'gobi')
```

output:

    {'fruit': 'apple', 'veggie': 'gobi'}
    My fruit of choice is apple.
    


```python
myfunc(cake = 'chocolate', veggie = 'gobi', sweets = 'carrot halwa')
```

output:

    {'cake': 'chocolate', 'veggie': 'gobi', 'sweets': 'carrot halwa'}
    There is no fruit of my choice here.
    

#Combination of both *args and **kwargs


```python
def myfunc(*args, **kwargs):  #order matters so *args is positional argument but **kwargs is keyword argument
    print(args)
    print(kwargs)
    print ("I would like {} {}.".format(args[0], kwargs['food'])) 


```


```python
myfunc(10,20,30, fruits = 'apple', food = 'eggs', juice = 'orange')
```

output:

    (10, 20, 30)
    {'fruits': 'apple', 'food': 'eggs', 'juice': 'orange'}
    I would like 10 eggs.
    


```python
def myfunc(*args):
    return [ num for num in args if num%2 == 0]
```


```python
def myfunc(*args):
    for num in args:
        if num % 2 ==0:
            print(num)
```

```python
myfunc(5,8,9,4,26,58,85)
```

output:

    [8, 4, 26, 58]



# write a function to capitalize alternate letters of the words entered


```python
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
```


```python
myfunc('Peeyush')
```

output:


    'pEeYuSh'




```python
def myfunc(*args):
    for args in args:
        print (args[0])
```


```python
myfunc('Vandana')
```

output:

    V
    


```python
def myfunc(*args):
    aA =''
    for item in args:
        print(item)
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
```


```python
myfunc('Peeyush,Vandana')
```

output:

    Peeyush,Vandana
    


output:

    'pEeYuSh,vAnDaNa'




```python
myfunc('Peeyush')
```

    Peeyush
    
output:

    'pEeYuSh'




```python
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
```


```python
result= myfunc('Peeyush','vandana')
print(result)
```

output:

    pEeYuShvAnDaNa
    


```python
def formatArrayOfString(*args):
    formatted_strings_array = []
    for input_string in args:
        print(input_string)
        formatted_string = ''
        for i in range (0, len(input_string)):
            if i%2 == 0:
                formatted_char = input_string[i].lower()
            else:
                formatted_char = input_string[i].upper()
            formatted_string = formatted_string + formatted_char
        formatted_strings_array.append(formatted_string)    
      
    return formatted_strings_array

```


```python
result = formatArrayOfString('peeyush', 'vandana')
print (result)
```

output:

    peeyush
    vandana
    ['pEeYuSh', 'vAnDaNa']
    

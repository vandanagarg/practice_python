
# coding: utf-8

# # Implementation of *args and **kwargs

# **Implementation of *args

# In[4]:


def myfunc(a,b):  
    #returns the 5% of the sum of a and b
    return sum((a,b)) * 0.05


# In[5]:


myfunc(40,60)


# #now in above the parameters are restricted and are positional arguments but to extend teh limit to take any n number of arguments , we use *args and *kwargs

# In[16]:


def myfunc(*args):  #here it will consider all values as a tuple for the number of parameters that are coming in
    return sum(args) * 0.05


# In[7]:


myfunc(5)


# In[17]:


myfunc(6,4)


# In[18]:


myfunc(8,2,5565,5562,22,12)


# In[21]:


def myfunc(*spam):  #its an arbitrary keyword not particulary args but * is important but better to use args #returns tuples
    print(spam)


# In[22]:


myfunc(8+2+5565+5562+22+12)


# In[23]:


myfunc(8,2,5565,5562,22,12) 


# **Implementation of **kwargs (**kwargs to retun a dictionary)

# In[31]:


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}.".format(kwargs['fruit']))
    else:
        print ("There is no fruit of my choice here.")


# In[32]:


myfunc(fruit = 'apple', veggie = 'gobi')


# In[33]:


myfunc(cake = 'chocolate', veggie = 'gobi', sweets = 'carrot halwa')


# **Combination of both *args and **kwargs**

# In[48]:


def myfunc(*args, **kwargs):  #order matters so *args is positional argument but **kwargs is keyword argument
    print(args)
    print(kwargs)
    print ("I would like {} {}.".format(args[0], kwargs['food'])) 



# In[35]:


myfunc(10,20,30, fruits = 'apple', food = 'eggs', juice = 'orange')


# In[44]:


def myfunc(*args):
    return [ num for num in args if num%2 == 0]


# In[39]:


def myfunc(*args):
    for num in args:
        if num % 2 ==0:
            print(num)


# In[47]:


myfunc(5,8,9,4,26,58,85)


# # write a function to capitalize alternate letters of the words entered

# In[96]:


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


# In[97]:


myfunc('Peeyush')


# In[24]:


def myfunc(*args):
    for args in args:
        print (args[0])


# In[25]:


myfunc('Vandana')


# In[38]:


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


# In[39]:


myfunc('Peeyush,Vandana')


# In[40]:


myfunc('Peeyush')


# In[41]:


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


# In[42]:


result= myfunc('Peeyush','vandana')
print(result)


# In[45]:


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


# In[46]:


result = formatArrayOfString('peeyush', 'vandana')
print (result)


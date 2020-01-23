# problem 4
# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

choice = input("Continue finding prime numbers (y/n)? ")
current = 1

def is_prime(n):
    # print("n is :" + str(n))
    # print(current)
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

while choice.lower().startswith('y'):
    current += 1
    # print("current in while is: " + str(current))
    while is_prime(current) == False:
        current += 1

    print("Next prime is: " + str(current))
    choice = input("Continue finding prime numbers (y/n)? ")


###################################################################################
def print_prime_num(prime_number):
    print("Prime number is: " + str(prime_number))

def next_prime_num():
    prime_number = 1
    print_prime_num(prime_number)
    while (input("Do you want to see next prime number? Yes or No") == "Yes" ):
        prime_number = get_prime_num(prime_number)
        print_prime_num(prime_number)

def get_prime_num(previous_prime_number):
    n = previous_prime_number + 1
    i = 2
    if n == 2:
        return n
    else:
        while i < n:
            if n % i == 0:
                # n += 1
                n = get_prime_num(n)
                # break
            elif n % i != 0:
                i += 1
        return n


# next_prime_num()
####################################################################################
def print_prime_num(prime_number):
    print("Prime number is: " + str(prime_number))

def next_prime_num():
    prime_number = 1
    print_prime_num(prime_number)
    while (input("Do you want to see next prime number? Yes or No") == "Yes" ):
        prime_number = check_next_prime_num(prime_number)
        # print_prime_num(prime_number)

def check_next_prime_num(prime_number):
    next_prime_num = prime_number + 1
    # is_prime = prime_num(next_prime_num)
    prime = prime_num(next_prime_num)
    print(prime)
    # if is_prime:
    #     print_prime_num(next_prime_num)
    #     return next_prime_num
    # else:
    #     next_prime_num = prime_num(n)
    #     print(next_prime_num)
    #     return next_prime_num

    #     next_prime_num += 1
    #     prime_num(next_prime_num)
    #     return next_prime_num


def prime_num(n):
    count = 0
    for i in range(1,n):
        if n%i == 0:
            count +=1
    if n==1 or count == 1:
        return n
    else:
        n += 1
        # print(n)
        prime_num(n)
        while prime_num(n):
            return n



# next_prime_num()


###############################################


# def prime_num(n):
#     count = 0
#     for i in range(1,n):
#         if n%i == 0:
#             count +=1
#     if n==1 or count == 1:
#         print("Entered number is prime")
#     else:
#         print("Entered number is not prime")
#
# # prime_num(1)



######################################################


def print_next_ten_num(num):
    for i in range(1,11):
        print(num + i)

# print_next_ten_num(2)


def is_even(num):
    return num % 2 == 0

# print(is_even(14))

def check_even():
    for i in range(1,11):
        if is_even(i):
            print(str(i) +" is even number.")
        else:
            print(str(i)+ " is odd number.")

# check_even()

def get_ten_even(num):
    even_list=[]
    i = num
    while i <= num+10:

        if is_even(i):
            even_list.append(i)
        i += 1
    return even_list

# print(get_ten_even(5))

# i = 1
# while i <= 10:
#     print(i)
#     i+=1


def get_ten_even2(num):
    even_list= []
    for i in range(num, num+10):
        if is_even(i):
            even_list.append(i)
    return even_list

# print(get_ten_even2(5))

def next_even_num(num):
    i =  num + 1
    while True:
        if is_even(i):
            return i
        else:
            i +=1

# print(next_even_num(1))
# print(next_even_num(2))


###########################################

def is_prime(num):
    count = 0
    for i in range(1,num):
        if num%i == 0:
            count+=1

    return num == 1 or count ==1

def next_prime(number):
    i = number +1
    while True:
        if is_prime(i):
            return "prime num is: "+ str(i)
        else:
            i += 1

# print(next_prime(4))
# print(next_prime(5))
print(next_prime(11))
print(next_prime(13))



#######################
#problem 3
#Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

#1st way:


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            # n //= i
            n = n/i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(15))


#2nd way:


def find_prime_fac(n):
    list_of_factors=[1]
    unique_list_factors = []
    i= 2
    while n > 1:
        if n % i == 0:
            list_of_factors.append(i)
            n = n / i
            i = i - 1
        i += 1

    for l in list_of_factors:
        if l not in unique_list_factors:
            unique_list_factors.append(l)

    return unique_list_factors


print(find_prime_fac(146))


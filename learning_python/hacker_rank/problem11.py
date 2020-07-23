# input(), eval() function
# In Python 2, the expression input() is equivalent to eval(raw_input(prompt))


# print(input())  # Python 3 just takes input, no evaluation
# print(eval(input()))
# # 1+2
# # 3

# company = 'HackerRank'
# website = 'www.hackerrank.com'
# print(input())
# print(eval(input()))
# # 'The company name: '+company+' and website: '+website
# # 'The company name: HackerRank and website: www.hackerrank.com'

x, k = (map(int, input().split()))
pol = input()

print(eval(pol) == k)
# 1 4
# x**3 + x**2 + x + 1

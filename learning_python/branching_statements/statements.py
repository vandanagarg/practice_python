''' Pass/ Continue/ Break statements '''

''' The break statement in Python terminates the current loop
and resumes execution at the next statement '''

print("\n break examples:")

# First Example
print("\n Example 1st \n")
my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        break
        my_sum += 1
    print("Inner sum", my_sum)
print("outer sum " + str(my_sum))

# Second Example
print("\n Example 2nd \n")
for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :', letter)
print('Outer Letter :', letter)

# Third Example
print("\n Example 3rd \n")
var = 10
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!", var)


''' The continue statement in Python returns the control to the beginning
of the while loop. It rejects all the remaining statements in the current
iteration of the loop and moves the control back to the top of the loop.
'''
print("\n Continue example:")

my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        continue
        my_sum += 1
    print("Inner sum", my_sum)
print("outer sum " + str(my_sum))


'''The pass statement in Python is used when a statement is required
syntactically but you do not want any command or code to execute.
The pass statement is a null operation; nothing happens when it executes
'''
print("\n pass example:")

my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        pass
        my_sum += 1
    print("Inner sum", my_sum)
print("outer sum " + str(my_sum))

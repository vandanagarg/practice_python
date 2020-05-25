''' Using Approximate Solutions find cube root
This is helpful when we don't have perfect cubes but still
we need to find a close enough answer '''

# 1st program
# cube = 27
cube = 8120601
# cube = 10000
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("num_guesses = ", num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)

''' num_guesses =  100000001
Failed on cube root of 10000 '''

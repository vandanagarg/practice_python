''' Using Bisection Search find cube root
The larger the search space it is useful to use bisection
search '''

# cube = 216
cube = .5
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print("num_guesses = ", num_guesses)
print(guess, "is close to the cube root of", cube)

''' This code is not applicable on numbers less than 1 '''

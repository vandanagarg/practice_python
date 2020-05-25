''' Using Guess and Check Algorithm find cube root
Usefull to find out perfect cubes '''

# 1st program
cube = 8
for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
# if using commas in print then type casting is not needed

# 2nd program
cube = -27
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(guess)
    print(cube, "is not a perfect cube.")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of", cube, "is", guess)

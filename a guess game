#building a guessing game using while loop #1. without any limit #2. With a limit

#1 without limit
secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")


#2 Lets limit the number of guess here using a few more variables


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE !")
else:
    print("You win!")


#lets see what happens if we dont use this out_of_guesses variable

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
#out_of_guesses = False

while guess != secret_word :
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        print("Out of guesses, YOU LOSE !")  # we need to have some variable so that here we can come out of this loop, else after 3 guesses it becomes an infinite loop
    
print("You win!")

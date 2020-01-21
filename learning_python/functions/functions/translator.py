#Tanslator
#Lets's say Giraffe Language
#vowels --> g  # in place of vowels g should come

#create a translate function
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  # or we can even use: if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
#
# o/p
#
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# Enter a phrase: to be or not to be
# tg bg gr ngt tg bg
#
# Process finished with exit code 0


# but the above programm doesn't handle the upper case so lets modify it with one more if else

def translate_caps(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate_caps(input("Enter a phrase: ")))

# o/p
#
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# Enter a phrase: On the spot, we went.
# Gn thg spgt, wg wgnt.
#
# Process finished with exit code 0

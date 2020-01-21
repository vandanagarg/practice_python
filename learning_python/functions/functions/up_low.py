#print nd bool chk

#Q3:   upper nd lower case in a sentence

def up_low(inp_string):
    lower_count = 0
    upper_count = 0

    for letter in inp_string:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            lower_count += 1
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper_count += 1
        else:
            continue
    print("Count of letters in Upper case is: " + str(upper_count))
    print("Count of letters in lower case is: " + str(lower_count))


up_low("Hello, I am Vandana Garg.")


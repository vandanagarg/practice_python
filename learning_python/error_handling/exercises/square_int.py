#problem 3

def square_int():
    while True:
        try:
            num_input = int(input("Enter a number: "))
            result = num_input ** 2
        except ValueError:
            print("Oh you have not entered a correct integer value.")
        except Exception as e:
            print(e)
            continue
        else:
            print("Square of your number is: " + str(result))
            break
        # finally:
        #     print("End of the program...")

square_int()

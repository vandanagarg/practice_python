#example error handling

def ask_for_integer():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("ohh! this is not a number.")
            continue
        else: #means there is no exception and user entered a correct int value
            print("Yes thank you.")
            break  #goes up-to its enclosing loop here while loop
        finally:  # here we can even put a finally block of code after else otherwise we can just keep either of these
            # but include break statement uin that in order to come out of infinite loop
            print("End of try/except/finally.")
            print("I will always run at the end!")

ask_for_integer()

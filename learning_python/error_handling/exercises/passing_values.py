#problem 1

try:
    for i in ["a","b","c"]:
        print(i**2)
except TypeError:
    print("Please pass a valid list of integers.")
except:
    print("Opps, you have passed some wrong value.")
finally:
    print("End of the program..")


#one.py

def func():
    print("FUNC() in one.py")

print("Top level in one.py")

if __name__ == "__main__":
    print("ONE.py is being run directly!")
else:
    print("ONE.py has been imported")
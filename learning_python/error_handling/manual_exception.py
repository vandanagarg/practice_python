##manually raising exceptions


try:
    f= open("currupt_file.txt")
    if f.name == "currupt_file.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

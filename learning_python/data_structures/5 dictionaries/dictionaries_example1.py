# Dictionaries
# Dictionaries are special structure in python that helps us to store special information what are called key value pairs.
# so we can create n number of such key value pairs and access them using the keys

# use case changing abbreviation of month to its full form . e.g: JAN -> January etc

monthConversions = {  # everything resides in these {} brackets  # all keys have to be unique
    "JAN": "January",
    "FEB": "February",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN": "June",
    "JUL": "July",
    "AUG": "August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December",  # last , is optional it work in both cases , but yes keys are case sensitive but can be anything a string, number etc
}

print(monthConversions["MAR"])       # 1st way  #if we pass some wrong key it throws error
print(monthConversions.get("DEC"))   # 2nd way
print(monthConversions.get("dec"))   #if we pass some wrong key it doesn't throw error but returns None and that's the benefit of using .get()  function
print(monthConversions.get("dec", "Not a valid key"))   # or we can return something we wish as default


# o/p
#
# C:\Users\as\Anaconda3\envs\Giraffe\python.exe C:/Users/as/PycharmProjects/Giraffe/app.py
# March
# December
# None
# Not a valid key
#
# Process finished with exit code 0

#using modules

import datetime


def user_age():
    input_user_age = int(input("Enter your age: "))
    #print(input_user_age)

    now = datetime.datetime.now()
    current_year = now.year

    diff_age = 100 - input_user_age
    year_100 = current_year + diff_age

    return ("You will be of 100 years in year " + str(year_100) + " .")

print(user_age())


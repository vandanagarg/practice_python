#Working with boolean True / False:
weekday = True
vacation = True

def sleep_in(weekday, vacation):
    if not weekday and not vacation:
        return True
    elif weekday == True and not vacation:
        return False
    elif not weekday and vacation == True:
        return True
    else:
        return False


print(sleep_in(False, True))


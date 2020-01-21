def film_category():
    user_age = int(input("Enter your age : "))
    print(user_age)

    if user_age in range(0,13):
        return "You can not watch any film."
    elif user_age in range(13, 19):
        return "You can watch animated movies. "
    else:
        return "You can watch any movie. "


print(film_category())


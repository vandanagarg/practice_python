# Problem 11
# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

import time


def alarm(n):
    print("Wait time:", n, "seconds.")
    time.sleep(n)  # Waits 'n' seconds before playing sound
    print("Time over")


def input_destinations(user_input):
    if user_input == '1':

        user_input = int(input("Enter the desired hours: "))

        wait_time = (user_input * 60) * 60
        alarm(wait_time)

    elif user_input == '2':

        user_input = int(input("Enter the desired minutes: "))

        wait_time = user_input * 60
        alarm(wait_time)

    elif user_input == '3':

        user_input = int(input("Enter the desired seconds: "))

        wait_time = user_input
        alarm(wait_time)

    elif user_input == '4':

        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        wait_time = ((hours * 60) * 60) + (minutes * 60) + seconds
        print(wait_time)
        alarm(wait_time)


def main():
    print("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
    main_input = input(": ")

    input_destinations(main_input)

    return


main()




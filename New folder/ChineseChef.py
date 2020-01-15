#lets say we have a chinese chef who has all qualities of generic chef (chef.py) and it makes something extra as well

# class chinesechef:
#     def make_chicken(self):
#         print("The chef makes a chicken.")
#
#     def make_salad(self):
#         print("The chef makes a salad.")
#
#     def make_special_dish(self):
#         print("The chef makes orange chicken.")
#
#     def make_fried_rice(self):
#         print("The chef makes fried rice.")


# In the above line of codes we have explicitly mentioned all the functions that we inside chef.py i.e: were already a part of generic chef class.
#Now in case we want to use inheritance(use existing generic class) this is how programm will look
#commented code above

from chef import Chef

class chinesechef(Chef):  # inheriting Chef function from chef file inside class chinesechef
#but now since the make_special_dish function is different in this class we will need to over ride that function here else it shows the generic function's o/p

    def make_special_dish(self):
        print("The chef makes orange chicken.")

    def make_fried_rice(self):
        print("The chef makes fried rice.")

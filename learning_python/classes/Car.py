# class User:

#     def __init__(self, name, email, id):
#       self.name = name
#       self.email = email
#       self.id = id 

#     @classmethod
#     def find(cls, id):
#         name = "Vandana"
#         email= "@xvg"
#         user_id = id
#         return cls(name, email, user_id)


# user1 = User.find(2)
# # print(user1)
# print(type(user1))

# # user2 = User()
# # print(type(user2))

# # user = User("Vandana", "xyz", 3)
# # print(user.name)
# # print(user.email)
# # print(user.id)




class Car:

    def __init__(self, model, color, car_type):
      self.model = model
      self.color = color
      self.car_type = car_type

    def print_car(self):
        print("model : " + self.model)
        print("color : " + self.color)
        print("car_type : " + self.car_type)

    @classmethod
    def suggest_car(cls):
        model = "Maruti Celerio X"
        color = "Black"
        car_type = "Petrol"

        return cls(model, color, car_type)
        



car1 = Car("Maruti XL6","Red", "Petrol")
car2 = Car("Maruti Vitara Brezza","White", "Deisel")
car3 = Car("Maruti Celerio X","Grey", "Gas")
car4 = Car("Maruti S-Presso","Black", "Petrol")


# car1.print_car()
print(Car.suggest_car())
car5 = Car.suggest_car()
car5.print_car()
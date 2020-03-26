import math


class Pizza:
    def __init__(self, radius, ingredients):  # constructor
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza with ({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(["Cheese", "Tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["Cheese", "Tomatoes", "ham", "mushrooms"])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


print(Pizza(4.5, ["Cheese", "veggies"]).area())
# 63.61725123519331

print(Pizza._circle_area)
# <function Pizza._circle_area at 0x10e4f3ca0>

print(Pizza._circle_area(4.5))
# 63.61725123519331

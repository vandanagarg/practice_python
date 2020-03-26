class Pizza:
    def __init__(self, ingredients, sauce):  # constructor
        self.ingredients = ingredients
        self.sauce = sauce

    def __repr__(self):
        return f'Pizza with {self.ingredients} , {self.sauce} '

    @classmethod
    def margherita(cls, sauce):
        money = "100 euro"
        return cls(["Cheese", "Tomatoes"], sauce, money)

    @classmethod
    def prosciutto(cls):
        return cls(["Cheese", "Tomatoes", "ham", "mushrooms"])


# print(Pizza(["Cheese", "Tomatoes", "olive"]))
# Pizza with (['Cheese', 'Tomatoes', 'olive'])

print(Pizza.margherita("tomato"))
# Pizza with (['Cheese', 'Tomatoes'])

# print(Pizza.prosciutto("mango"))
# Pizza with (['Cheese', 'Tomatoes', 'ham', 'mushrooms'])

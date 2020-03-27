class Pizza:
    def __init__(self, ingredients, sauce, money):  # constructor
        self.ingredients = ingredients
        self.sauce = sauce
        self.money = money

    def __repr__(self):
        return f'Pizza with {self.ingredients} , {self.sauce} \
        costing {self.money}'

    @classmethod
    def margherita(cls, sauce):
        money = "100 euro"
        return cls(["Cheese", "Tomatoes"], sauce, money)

    @classmethod
    def prosciutto(cls):
        return cls(["Cheese", "Tomatoes", "ham", "mushrooms"], "", "")


print(Pizza(["Cheese", "Tomatoes", "olive"], "", ""))
# Pizza with (['Cheese', 'Tomatoes', 'olive'])

print(Pizza.margherita("tomato"))
# Pizza with (['Cheese', 'Tomatoes'])

print(Pizza.prosciutto())
# Pizza with (['Cheese', 'Tomatoes', 'ham', 'mushrooms'])

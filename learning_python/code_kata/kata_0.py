''' Problem: To make a price cart for a shopping mall
The price is decided on the number of units of product you purchase.

'''
class PriceCalculator():
    
    DICT_ITEM_COST = {
        "milk": {"price": 59, "offer": {"quantity": 3, "price": 150}},
        "curd": {"price": 181}, 
        "apple": {"price": 310},
        "cream": {"price": 281, "offer": {"quantity": 4, "price": 700}},
        "biscuit": {"price": 200},
        "orange": {"price": 600},
        "humus": {"price": 300}
    }

    def __init__(self, purchase_items_dict):
        self.purchase_items_dict = purchase_items_dict

    def cal_sp(self):
        selling_price = 0
        for (item_name, quantity) in purchase_items_dict.items():
            price = PriceCalculator.DICT_ITEM_COST[item_name]["price"] * quantity
            selling_price = selling_price + price
        return selling_price


purchase_items_dict = {"orange": 2, "humus": 1}
calculator = PriceCalculator(purchase_items_dict)
print(calculator.cal_sp())

# offer_dict = {"milk": {"quantity": 3, "price": 150}, "cream": {"quantity": 4, "price": 700}}
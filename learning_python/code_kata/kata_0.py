''' Problem: To make a price cart for a shopping mall
The price is decided on the number of units of product you purchase.

'''
class PriceCalculator():
    
    DICT_ITEM_COST = {
        "milk": 59,
        "apple": 310,
        "curd": 181, 
        "cream": 281,
        "biscuit": 200,
        "orange": 600,
        "humus": 300
    }

    def __init__(self, purchase_items_dict):
        self.purchase_items_dict = purchase_items_dict

    def cal_sp(self):
        selling_price = 0
        for (item_name,quantity) in purchase_items_dict.items():
            price = PriceCalculator.DICT_ITEM_COST[item_name] * quantity
            selling_price = selling_price + price
        return selling_price


purchase_items_dict = {"orange": 2, "humus": 1}
calculator = PriceCalculator(purchase_items_dict)
print(calculator.cal_sp())
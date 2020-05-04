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
        for (item_name, order_quantity) in purchase_items_dict.items():
            item_price = PriceCalculator.DICT_ITEM_COST[item_name]["price"]
            try:
                offer_key = PriceCalculator.DICT_ITEM_COST[item_name]["offer"]
                offer_quantity = offer_key["quantity"]
                if (offer_key):
                    if order_quantity < offer_quantity:
                        price = item_price * order_quantity
                    else:
                        offer_applied = order_quantity//offer_quantity
                        extra = order_quantity%offer_quantity
                        price = offer_key["price"] * offer_applied + item_price * extra
            except KeyError:
                price = item_price * order_quantity
            selling_price = selling_price + price
        return selling_price


# purchase_items_dict = {"orange": 2,  "milk": 1, "humus": 1}
# purchase_items_dict = {"orange": 2, "humus": 1}
# purchase_items_dict = {"milk": 1}
# purchase_items_dict = {"milk": 3}
purchase_items_dict = {"milk": 5, "cream": 2, "orange": 2, "humus": 1}
# purchase_items_dict = {"cream": 4, "milk": 3}
calculator = PriceCalculator(purchase_items_dict)
print(calculator.cal_sp())

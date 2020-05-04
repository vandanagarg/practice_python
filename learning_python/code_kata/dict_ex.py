DICT_ITEM_COST = {
        "milk": {"price": 59, "offer": {"quantity": 3, "price": 150}},
        "curd": {"price": 181},
        "apple": {"price": 310},
        "cream": {"price": 281, "offer": {"quantity": 4, "price": 700}},
        "biscuit": {"price": 200},
        "orange": {"price": 600},
        "humus": {"price": 300}
    }

purchase_items_dict = {"milk": 5, "cream": 2, "orange": 2, "humus": 1}

# a_dict.get('missing_key', 'default value')
for (item_name, order_quantity) in purchase_items_dict.items():
    print(DICT_ITEM_COST[item_name].keys())
    print(DICT_ITEM_COST[item_name].get("offer", None))
    if "offer" in DICT_ITEM_COST[item_name]:
        print(item_name)
    else:
        print("no item")

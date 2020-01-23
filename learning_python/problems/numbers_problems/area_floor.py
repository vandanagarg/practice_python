# Problem 5
#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.


def area_floor(width=1, height=1):
    return float(width * height)


def cost(amount):
    return float(area_floor() * amount)


print(cost(4))


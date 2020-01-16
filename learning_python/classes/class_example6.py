class User:

    def __init__(self,name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.addresses = []

    def add_address(self, house_no, area, place):
        self.house_no = house_no
        self.area = area
        self.place = place


    def __str__(self):
        print(" User name is: " + self.name)
        print(" User email is: " + self.email)
        print(" User age is: " + str(self.age))

        for index in range(0,len(self.addresses)):
            print(" User address " + str(index + 1) + " :")
            address_index = self.addresses[index]
            # print(address_index.house_no)
            print("User House No. is :" + address_index.house_no)
            print("User Area is : " + address_index.area)
            print("User Place is : " + address_index.place)

my_user = User("Vandana", "er.va", 27)

# home_address = User.add_address(my_user, "66", "ward 12", "Kurali")
# current_address = User.add_address(my_user, "0401", "str. praiser kommune", "Berlin")
# picky_address = User.add_address(my_user, "453", "Geeta Bhawan ", "Moga")


my_user.__str__()


class Address:

    def __init__(self, house_no, area, place):
        self.house_no = house_no
        self.area = area
        self.place = place

home_address = Address("66", "ward 12", "Kurali")
current_address = Address("0401", "str. praiser kommune", "Berlin")

picky_address = Address("453", "Geeta Bhawan ", "Moga")



print(my_user.name)
print(my_user.email)
my_user.age = 28
print( my_user.age)


my_user.addresses.append(home_address)
my_user.addresses.append(current_address)
my_user.addresses.append(picky_address)


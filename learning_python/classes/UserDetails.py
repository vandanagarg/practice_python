class UserDetails:

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

my_user = UserDetails("Vandana", "er.va", 27)

home_address = UserDetails.add_address(my_user, "66", "ward 12", "Kurali")
current_address = UserDetails.add_address(my_user, "0401", "str. praiser kommune", "Berlin")
picky_address = UserDetails.add_address(my_user, "453", "Geeta Bhawan ", "Moga")


my_user.__str__()



from faker import Faker
fake_data = Faker()


#create persons object with name, address etc

class Customers:

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    # special method __repr__() to display data associated with object
    def __repr__(self):
        return "name: {}, address: {}, email: {}".format(self.name, self.address, self.email)

#instance of Customers class using fake data
customer1 = Customers(fake_data.name(), fake_data.address(), fake_data.email())
print("customer1: " + str(customer1))

#generate list of customers class objects with fake data
customers_list= []
for i in range (10):
    customers_list.append(Customers(fake_data.name(), fake_data.address(), fake_data.email()))

for i in customers_list:
    print("\n", i, "\n")




#Python generate fake data

from faker import Faker
fake_data = Faker()

#create fake name
name = fake_data.name()
print(name)

#create fake address
address = fake_data.address()
print(address)

#create fake email
email = fake_data.email()
print(email)


#create fake profile
profile = fake_data.simple_profile()

for k,v in profile.items():
    print('{}:{}'.format(k,v))


#display name, address, email
print("Name: {}, Address: {}, Email: {}".format(name,address,email))

#generate a  larger set of fake data

for _ in range(0,10):
    print(fake_data.name())


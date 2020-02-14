from faker import Faker
fake_data = Faker()

#create fake name
name = fake_data.name()
# print(name)

#function to fill a list with data
#change .name() to another data type for other data type options

def create_name_list(how_many):
    names= []
    for _ in range(0,how_many):
        names.append(fake_data.name())
    return names


print(create_name_list(5))

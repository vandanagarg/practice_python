from faker import Faker
fake_data = Faker()

data_rows = ("Name: {}, Address: {}, Email: {}".format(fake_data.name(), fake_data.address(), fake_data.email()))
print(data_rows)

print(type(data_rows))


def create_data_list(how_many):
    main_data_list = []
    for _ in range(0, how_many):
        data_list = [fake_data.name(), fake_data.address(), fake_data.email()]
        main_data_list.append(data_list)

    return main_data_list

print(create_data_list(5))


from faker import Faker
fake_data = Faker()

def create_name_list(how_many):
    names = []
    for _ in range(0,how_many):
        names.append(fake_data.name())
    return names

# write fake data to csv file

import csv

with open("new_data.csv", "w", newline="")  as csvfile:
    csv_fake_data = csv.writer(csvfile)
    for i in create_name_list(10):
        csv_fake_data.writerow([i])

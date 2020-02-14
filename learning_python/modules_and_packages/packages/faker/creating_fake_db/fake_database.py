#use fake data with sqlite3 to create database file
#import, connection, cursor, table, edit, save,close

import mysql.connector
from faker import Faker
fake_data = Faker()


class DatabaseAdapter:
    DB_CONFIG = {
        'host': "localhost",
        'user': "root",
        'passwd': "testing123"
    }

    def __init__(self):
        self.adapter = mysql.connector.connect(**self.DB_CONFIG)

    def setup_database(self):
        client = self.adapter.cursor()
        client.execute("Drop Database faker_db")
        client.execute("Create Database faker_db")
        client.execute("USE faker_db")
        client.execute("\
        CREATE TABLE fake_table \
            ( \
                name     VARCHAR(255), \
                address      VARCHAR(255), \
                email VARCHAR(255)\
            ) \
        ")

    def create_data_list(self, row_count):
        main_data_list = []
        for _ in range(0, row_count):
            data_list = [fake_data.name(), fake_data.address(), fake_data.email()]
            main_data_list.append(data_list)
        return main_data_list

    def insert_data(self, data_rows):
        client = self.adapter.cursor()
        client.execute("USE faker_db")

        sqlform = "Insert into fake_table(name, address, email) values(%s,%s,%s)"

        client.executemany(sqlform, data_rows)

        self.adapter.commit()

    def load_data(self):
        self.setup_database()
        data_rows = self.create_data_list(5)
        self.insert_data(data_rows)


db_client = DatabaseAdapter()
db_client.load_data()

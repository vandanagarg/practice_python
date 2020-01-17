import mysql.connector


class DatabaseAdapter:
    DB_CONFIG = {
        'host': "",
        'user': "",
        'passwd': ""
    }

    def __init__(self):
        self.adapter = mysql.connector.connect(**self.DB_CONFIG)

    def setup_database(self):
        client = self.adapter.cursor()
        client.execute("Create Database database_etl")
        client.execute("USE database_etl")
        client.execute("\
        CREATE TABLE user_account_details \
            ( \
                id             INT(10) NOT NULL PRIMARY KEY, \
                first_name     VARCHAR(255), \
                last_name      VARCHAR(255), \
                account_number VARCHAR(25) NOT NULL, \
                amount_in_cents   DOUBLE NOT NULL \
            ) \
            DEFAULT CHARACTER SET=utf8 \
        ")

    def insert_data(self, data_rows):
        client = self.adapter.cursor()
        client.execute("USE database_etl")

        sqlform = "Insert into user_account_details(id,first_name,last_name,account_number,amount_in_cents) values(%s,%s,%s,%s,%s)"
        client.executemany(sqlform, data_rows)
        self.adapter.commit()

    def load_data(self, data_rows):
        self.setup_database()
        self.insert_data(data_rows)

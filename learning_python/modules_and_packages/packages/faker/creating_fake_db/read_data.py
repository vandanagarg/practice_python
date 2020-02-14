import mysql.connector

adapter = mysql.connector.connect(user='root', password="testing123", database='faker_db')
client = adapter.cursor()

client.execute("Select name, address from fake_table")

result = client.fetchall()
# print(result)
# for i in result:
#     print(i)

# printing column names
# print(client.column_names)

# num_fields = len(client.description)
# print(client.description)

# field_names = [i[0] for i in client.description]
# print(field_names)
#

# reading data as a list of dictionaries
row_list = []

for i in range(0, len(result)):
    table_dict = {}
    for row in range(0, len(result[i])):
        table_dict[client.column_names[row]] = result[i][row]
    row_list.append(table_dict)
print(row_list)


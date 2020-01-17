import csv_reader
import database_adapter

csv_reader = csv_reader.CsvReader('cleaned_api_response.tsv')
data_rows = csv_reader.parse()

db_client = database_adapter.DatabaseAdapter()
db_client.load_data(data_rows)

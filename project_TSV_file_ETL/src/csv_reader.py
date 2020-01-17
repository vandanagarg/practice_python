import codecs
import csv
import re


class CsvReader:
    TEMP_FORMATTED_FILE_NAME = 'utf_8_encoded_data.tsv'

    def __init__(self, file_name):
        self.file_name = file_name

    def process_file_format(self):
        with codecs.open(self.file_name, 'rU', 'utf-16le') as raw_file:
            raw_data = raw_file.read()
            with codecs.open(CsvReader.TEMP_FORMATTED_FILE_NAME, 'w', 'utf-8') as temp_formatted_file:
                for line in raw_data:
                    temp_formatted_file.write(line.replace('\x00', ''))

    def format_row(self, row):
        negative = row[4][0] == '-'
        amount_in_cents = int(
            ''.join(
                map(
                    str, re.findall(r'\b\d+\b', row[4])
                )
            )
        ) * 100
        if negative:
            row[4] = '-' + str(amount_in_cents)
        else:
            row[4] = str(amount_in_cents)

    def parse(self):
        self.process_file_format()
        file_rows = []
        with open(CsvReader.TEMP_FORMATTED_FILE_NAME) as tsvfile:
            next(tsvfile)
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                self.format_row(row)
                file_rows.append(row)
        return file_rows

import csv


def read_column_from_csv(file_path, column_name):
    values = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values.append(row[column_name])
    return values

import csv
import json

csv_file_ads = 'ads.csv'
json_file_ads = 'ads.json'
ads_model = 'ads.ad'

csv_file_catetories = 'categories.csv'
json_file_categories = 'categories.json'
categories_model = 'ads.category'


def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:

    with open(csv_file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        data: list = [
            {'model': model,
             'pk': int(row['id']) if row.get('id') else int(row['Id']),
             'fields': {
                 key: replace_values(value) for key, value in row.items() if key != 'id' and key != 'Id'}
             }
            for row in reader
        ]

    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    return f'Data from csv ({csv_file_path}) converted to json ({json_file_path})'


def replace_values(value):
    if value.isdigit():
        return int(value)
    if value == 'TRUE' or value == 'FALSE':
        return bool(value)

    return value


if __name__ == '__main__':
    print(csv_to_json(csv_file_ads, json_file_ads, ads_model))
    print(csv_to_json(csv_file_catetories, json_file_categories, categories_model))

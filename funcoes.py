import csv
import re
from datetime import datetime

def open_file(file_name: str) -> list[dict]:
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def drop_invalid_measures(list) -> tuple:
    product_list = []
    droped_rows = 0
    for row in list:
        if None in (row['product_length_cm'], row['product_height_cm'], row['product_width_cm']):
            droped_rows += 1
            continue
        product_list.append(row)
    return product_list, droped_rows

def fix_product_null_values(list, new_weigth) -> tuple:
    total_fixed_categories = 0
    total_fixed_weights = 0
    for row in list:
        if not row['product_category_name']:
            row['product_category_name'] = 'sem categoria'
            total_fixed_categories += 1

        if not row['product_weight_g']:
            row['product_weight_g'] = new_weigth
            total_fixed_weights += 1

    return total_fixed_categories, total_fixed_weights

def mean_product_weight(list):
    total_weight = 0
    for row in list:
        if row['product_weight_g']:
            total_weight += int(row['product_weight_g'])
    mean_weight = total_weight / len(list)
    return mean_weight

def fix_category_names(list):
    for row in list:
        text_to_clear = row['product_category_name']
        text_to_clear = text_to_clear.lower().strip()
        row['product_category_name'] = re.sub(r'[^a-zà-úA-ZÀ-Ú0-9 ]','', text_to_clear)

def fix_approval_date(list):
    for row in list:
        raw_date = row['order_approved_at']
        if raw_date:
            formated_date = datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
            row['order_approved_at'] = formated_date

# contruindo o relatório
def order_status_affects_delivered_date(list) -> tuple:
    date_null_canceled = 0
    date_null_not_canceled = 0
    for row in list:
        if row['order_delivered_customer_date']:
            continue

        if not row['order_delivered_customer_date'] and row['order_status'] == 'canceled':
            date_null_canceled += 1
        else:
            date_null_not_canceled += 1

    return date_null_canceled, date_null_not_canceled


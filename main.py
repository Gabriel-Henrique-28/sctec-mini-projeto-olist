from funcoes import *

PRODUCTS_FILE_PATH = 'data/olist_products_dataset.csv'
ORDERS_FILE_PATH = 'data/olist_orders_dataset.csv'

# limpeza do arquivo de produtos
print('Processando o arquivo de produtos...')
product_list = open_file(PRODUCTS_FILE_PATH)
product_rows_count = len(product_list)
new_product_list, droped_rows = drop_invalid_measures(product_list)
mean_weight = mean_product_weight(new_product_list)
total_fixed_categories, total_fixed_weights = fix_product_null_values(new_product_list, mean_weight)
fix_category_names(new_product_list)

# limpeza do arquivo de pedidos
print('Processando o arquivo de pedidos...')
data = open_file(ORDERS_FILE_PATH)
orders_rows_count = len(data)
fix_approval_date(data)

# relatório
print('Gerando o relatório...')
data = open_file(ORDERS_FILE_PATH)
date_null_canceled, date_null_not_canceled = order_status_affects_delivered_date(data)
total_orders_canceled = date_null_canceled + date_null_not_canceled
percentage = (date_null_canceled * 100) / total_orders_canceled
total_processed_rows = product_rows_count + orders_rows_count
total_fixed_nulls = total_fixed_categories + total_fixed_weights
print('Relatório gerado com sucesso!')

print('----------------------- Relatório -----------------------')
print(f'Total de linhas processadas: {total_processed_rows}')
print(f'Total de categorias nulas corrigidas: {total_fixed_categories}')
print(f'Total de pesos nulos corrigidos: {total_fixed_weights}')
print(f'Total de valores nulos corrigidos: {total_fixed_nulls}')
print(f'Total de registros nulos deletados: {droped_rows}')
print(f'Total de pedidos cancelados: {total_orders_canceled}')
print(f'De todos os pedidos com data de entrega nula, {percentage:.2f}% tinham o status de cancelado')
import csv
import re
from datetime import datetime

# Abre o arquivo utilizando o caminho informado pelo parâmetro
# retorna uma lista contendo todos os registros do arquivo csv aberto
def open_file(file_path: str) -> list[dict]:
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# recebe a lista de produtos e remove as colunas que tiverem alguma medida de tamanho fisico nulas, retornando uma nova lista com as linhas removidas
# foi optado a exclução das linhas com medidas nulas, pois por se tratar de 3 campos que se relacionam diretamente (altura, largura e comprimento)
# poderia haver muitas inconsistencias se fosse preenchido a média de cada campo
# outro motivo que contribuiu para esta decisão foi o fato de ao remover produtos com medidas nulas não causar uma grande perda de dados na base
def drop_invalid_measures(list) -> tuple:
    product_list = []
    droped_rows = 0
    for row in list:
        if None in (row['product_length_cm'], row['product_height_cm'], row['product_width_cm']):
            droped_rows += 1
            continue
        product_list.append(row)
    return product_list, droped_rows

# Recebe a lista de produtos e um valor padrão para linhas que tiverem um peso nulo
# retorna uma tupla com o numero total de categorias ajustadas e total de pesos ajustados
# foi optado pelo mantimento das linhas com pesos nulos, aplicando um valor padrão que neste caso é o peso médio
# pois por se tratar de apenas um dado físico independente não haveria nenhuma grande inconsistencia
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

# recebe a lista de produtos e calcula o peso médio dos produtos, retornando o peso médio em um numero decimal (float)
def mean_product_weight(list) -> float:
    total_weight = 0
    for row in list:
        if row['product_weight_g']:
            total_weight += int(row['product_weight_g'])
    mean_weight = total_weight / len(list)
    return mean_weight

# recebe a lista de categorias e ajusta o nome das categorias para que não tenham espaço em branco nos extremos e não tenham caracteres especiais
def fix_category_names(list):
    for row in list:
        text_to_clear = row['product_category_name']
        text_to_clear = text_to_clear.lower().strip()
        row['product_category_name'] = re.sub(r'[^a-zà-úA-ZÀ-Ú0-9 ]','', text_to_clear)

# recebe a lista de pedidos e ajusta a data de aprovação formatando para o padrão dd/mm/YYYY
def fix_approval_date(list):
    for row in list:
        raw_date = row['order_approved_at']
        if raw_date:
            formated_date = datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
            row['order_approved_at'] = formated_date

# recebe a lista de pedidos e verifica dos pedidos com datas nulas quantos foram cancelados e quantos não foram
# retorna uma tupla com o total de pedidos com data de entrega nulas que tinha status de cancelado e quantos tinham data nula mas não tinha status canelado
# método criado puramente para gerar os dados para o relatório final
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
import json

# Загрузка данных из файла f.json
with open('f.json', 'r') as file:
    data = json.load(file)

# Словари для хранения результатов
category_count = {}
category_sales = {}

for item in data:
    category = item['category']
    price = item['price']

    # Подсчитаем количество предметов в каждой категории (учитываем дубликаты)
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1

    # Подсчитаем общую сумму продаж для каждой категории
    if category in category_sales:
        category_sales[category] += price
    else:
        category_sales[category] = price

# Выводим результаты
print("Количество предметов по категориям:", category_count)
print("Общая сумма продаж по категориям:", category_sales)

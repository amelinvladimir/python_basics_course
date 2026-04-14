import csv

# Получение списком
with open('users.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"Имя: {row[0]}, Возраст: {row[1]}")
        
# Получение данных словарем      
with open('users.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)  # Первая строка автоматически становится ключами
    for row in reader:
        print(f"Имя: {row['Имя']}, Возраст: {row['Возраст']}")
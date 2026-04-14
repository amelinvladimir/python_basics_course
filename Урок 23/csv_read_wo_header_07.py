import csv

with open('users wo_names.csv', 'r', encoding='utf-8', newline='') as f:
    # Если в файле нет заголовков:
    reader = csv.DictReader(f, fieldnames=['name', 'age'])
    for row in reader:
        print(f"Имя: {row['name']}, Возраст: {row['age']}")
import csv

data = [
    ['Анна', 22, 'Москва'],
    ['Борис', 31, 'Казань'],
    ['Вера', 27, 'Новосибирск']
]

with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])  # Заголовок
    writer.writerows(data)                    # Данные
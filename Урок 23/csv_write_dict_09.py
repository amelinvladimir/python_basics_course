import csv

users = [
    {'name': 'Анна', 'age': 22, 'city': 'Москва'},
    {'name': 'Борис', 'age': 31, 'city': 'Казань'}
]

fieldnames = ['name', 'age', 'city']

with open('output_dict.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)
# PUT-запрос
# Изменим пользователя.

import requests

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json={
        "name": "Новое имя"
    }
)

print(response.json())
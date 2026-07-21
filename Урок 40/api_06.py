# POST-запрос
# Создадим пользователя.

import requests

new_user = {
    "name": "Владимир",
    "age": 40
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

print(response.status_code)
print(response.json())
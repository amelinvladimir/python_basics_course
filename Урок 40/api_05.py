# Передача параметров

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params={
        "id": 3
    }
)

print(response.json())

# Что реально отправится
# https://jsonplaceholder.typicode.com/users?id=3
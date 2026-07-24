# pip install requests

import requests

response = requests.post(
    "http://127.0.0.1:8000/users",
    json={
        "name": "Владимир",
        "age": 40
    }
)

print(response.json())
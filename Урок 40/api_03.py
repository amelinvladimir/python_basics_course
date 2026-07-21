# Преобразование JSON в словарь
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

# плохо
print(response.text)

# хорошо
user = response.json()

print(user)
print(user["name"])
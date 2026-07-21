# Заголовки (Headers)
import requests

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Authorization": "Bearer TOKEN"
}

response = requests.get(
    url,
    headers=headers
)
print(response.text)
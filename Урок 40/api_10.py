# Таймауты
import requests

url = "https://jsonplaceholder.typicode.com/users"

# Плохой код:
# Программа может зависнуть.
# response = requests.get(url)

# Лучше:
response = requests.get(
    url,
    timeout=5
)
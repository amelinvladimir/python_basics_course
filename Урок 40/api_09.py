# Обработка ошибок
import requests

url = "https://1jsonplaceholder.typicode.com/users"

# Плохой вариант:
# response = requests.get(url)
# data = response.json()

# Если сервер недоступен:
# ConnectionError

# Правильный вариант
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Ошибка:", e)
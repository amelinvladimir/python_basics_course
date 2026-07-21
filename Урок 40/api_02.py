# Что такое response
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(f'status code: {response.status_code}')
print(f'text: {response.text}')
print(f'json(): {response.json()}')
print(f'headers: {response.headers}')


# Основные коды ответа

# 200
# Все хорошо.

# 201
# Объект создан.

# 400
# Ошибка клиента.

# 401
# Нет авторизации.

# 403
# Доступ запрещен.

# 404
# Не найдено.

# 500
# Ошибка сервера.
# https://site.com/users/5

# {
#     "id": 5,
#     "name": "Иван"
# }

# pip install requests

# https://jsonplaceholder.typicode.com

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/2"
)

print(response.text)
import json

user = {
    "name": "Мария",
    "age": 31,
    "roles": ["admin", "data_engineer"],
    "active": True,
    "balance": None
}

# Python → JSON-строка
json_str = json.dumps(user, ensure_ascii=False, indent=4)
print(json_str)

# JSON-строка → Python
parsed = json.loads(json_str)
print(type(parsed))
print(parsed["roles"])
print(parsed)
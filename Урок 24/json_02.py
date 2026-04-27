import json

user = {
    "name": "Мария",
    "age": 31,
    "roles": ["admin", "data_engineer"],
    "active": True,
    "balance": None
}

# Запись
with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=2)
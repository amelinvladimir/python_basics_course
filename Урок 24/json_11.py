import json

with open("big.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(type(config))

items = config.get("items", [])
print(type(items))

print(type(items[0]))
print(items[0])

tags = items[0].get("tags", []) if items else []

print(type(tags))
print(tags)
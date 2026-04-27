import json

with open("big.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(config["name"])
print(config.get('name'))
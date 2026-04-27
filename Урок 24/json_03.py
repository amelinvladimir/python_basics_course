import json

with open("settings.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(config["name"])
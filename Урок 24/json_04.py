import json

broken = '{"status": "ok", "data": }'  # синтаксическая ошибка

try:
    json.loads(broken)
except json.JSONDecodeError as e:
    print(f"❌ Ошибка JSON: {e}")
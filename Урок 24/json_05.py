from datetime import datetime
import json

def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return sorted(list(obj))
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

data = {"created": datetime.now(), "tags": {"python", "etl"}}

print(json.dumps(data, default=custom_serializer, indent=2))
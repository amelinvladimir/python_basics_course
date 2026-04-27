import json

print(json.dumps({'6': 7, '4': 5, '3': {5: 3, 4: 2}}, sort_keys=True, indent=4))
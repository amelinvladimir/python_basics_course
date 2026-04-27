import json

weird_json = '{"x": 1, "x": 2, "x": 3}'
j = json.loads(weird_json)
print(j)
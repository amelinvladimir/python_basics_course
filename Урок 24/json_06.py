import json

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'), indent=4))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'), indent=8))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'), indent=''))

import json


with open('users.json', 'r') as f:
    data = json.load(f)
    data.append({"id": 2, "name": "Vladik", "role": "admin"})
with open('users.json', 'w') as f:
    json.dump(data, f)
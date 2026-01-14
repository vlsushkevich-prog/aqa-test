import json


users = [{'id': 1, 'name': 'Sasha', 'role': 'admin'}]

with open('users.json', 'w') as f:
    json.dump(users, f)
import yaml


users = [{'id': 1, 'name': 'Sasha', 'role': 'admin'}]

with open('users.yaml', 'w') as f:
    yaml.safe_dump(users, f, sort_keys=False)
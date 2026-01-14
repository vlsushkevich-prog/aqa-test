import yaml


with open('users.yaml', 'r') as f:
    data = yaml.safe_load(f)
    data.append({"id": 2, "name": "Vladik", "role": "admin"})
with open('users.yaml', 'w') as f:
    yaml.safe_dump(data, f, sort_keys=False)
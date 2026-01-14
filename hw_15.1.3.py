import json


with open('test_results.json', 'r') as f:
    results = json.load(f)
    passed_percentage = results['passed'] / results['total'] * 100

print(passed_percentage)
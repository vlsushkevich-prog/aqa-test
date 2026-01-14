import yaml


with open('test_results.yaml', 'r') as f:
    results = yaml.safe_load(f)
    passed_percentage = results['passed'] / results['total'] * 100

print(passed_percentage)
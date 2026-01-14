import yaml


results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}

with open('test_results.yaml', 'w') as f:
    yaml.safe_dump(results, f, sort_keys=False)
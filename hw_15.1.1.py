import json


results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}

with open('test_results.json', 'w') as f:
    json.dump(results, f)
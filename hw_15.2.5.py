import yaml
from dummy_test_runner import *


with open('dummy_test_results.yaml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


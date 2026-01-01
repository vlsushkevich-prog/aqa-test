import re


def is_valid_date(date):
    return True if re.match(r'\b\d{4}-\d{2}-\d{2}\b', date) else False

print(is_valid_date('2025-12-28'))
print(is_valid_date('25-12-28'))
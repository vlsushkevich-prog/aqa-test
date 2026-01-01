import re


def status_code(log):
    return re.search(r'HTTP/1.1" (\d+)', log).group(1)

example = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'

print(status_code(example))
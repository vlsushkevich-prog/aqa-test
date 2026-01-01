import re


def find_id(url):
    return re.search(r'/api/v1/users/(\d+)/orders/(\d+)', url).groups()

print(find_id('/api/v1/users/123/orders/456'))
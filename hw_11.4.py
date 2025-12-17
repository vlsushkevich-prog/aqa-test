from enum import Enum


class Environment(Enum):
    DEV = 'https://dev.example.com'
    PROD = 'https://example.com'
    STAGE = 'https://stage.example.com'

def get_base_url(environment):
    match environment:
        case Environment.DEV:
            return Environment.DEV.value
        case Environment.PROD:
            return Environment.PROD.value
        case Environment.STAGE:
            return Environment.STAGE.value

print(get_base_url(Environment.DEV))
print(get_base_url(Environment.PROD))
print(get_base_url(Environment.STAGE))
import re


def dict_creator(data):
    return dict(re.findall(r'(\w+)=([^;]+)', data))

example = ('name=John; city=London; age=30')
print(dict_creator(example))
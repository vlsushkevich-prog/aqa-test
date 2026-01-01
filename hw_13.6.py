import re


def space_formatter(string):
    formatted_string = re.sub(r'\s+', ',', string)
    return formatted_string

data = 'one two    three\tfour\nfive'
print(space_formatter(data))

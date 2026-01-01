import re


def splitter(string):
    return re.split(r'[, ;]', string)

print(splitter('one,two;three four'))
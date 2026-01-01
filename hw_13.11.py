import re


def tag_remover(s):
    return re.sub(r'<[^>]+>', '', s)

example = "<p>Hello <b>world</b>!</p>"
print(tag_remover(example))
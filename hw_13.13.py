import re


def find_phones(string):
    return re.findall(r'(?:\+\d-\d{3}-\d{3}-\d{2}-\d{2})|'
                      r'(?:\d \(\d{3}\) \d{3}-\d{2}-\d{2})', string)

text = 'Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77.'
print(find_phones(text))






import re


def get_domains(emails):
    return [re.search(r'@[^@]+\.+[^@]{2,}', email).group() for email in emails]

print(get_domains(["a@test.com", "b@mail.ru", "user@sub.example.org"]))

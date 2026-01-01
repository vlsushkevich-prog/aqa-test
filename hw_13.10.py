import re


def is_strong_password(password):
    if (re.search(r'[A-Z]', password)
            and re.search(r'[0-9]', password)
            and len(password) >= 8):
        return True
    else:
        return False

print(is_strong_password('Abcdef12'))
print(is_strong_password('abcdef12'))
print(is_strong_password('Abcdefgh'))

import time
import random


def process_files():
    print('Обработка файлов...')
    time.sleep(3)
    print('Готово!')
    return 'processed'

def read_config(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def generate_password(length=8):
    chars = 'abc123'
    return ''.join(random.choice(chars) for i in range(length))
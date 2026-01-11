def read_first_chars(path, n):
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read(n))

read_first_chars('app.log', 5)
def filter_file(src, dst, keyword):
    with open(src, 'r', encoding='utf-8') as f:
        data = f.readlines()

    with open(dst, 'w', encoding='utf-8') as f:
        for line in data:
            if keyword in line:
                f.write(line)

filter_file('app.log', 'app.log1', 'Test')
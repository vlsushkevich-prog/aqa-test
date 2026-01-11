def sum_from_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        result = 0
        for line in f:
            result += int(line.strip())
        print(result)

sum_from_file('app.log1')
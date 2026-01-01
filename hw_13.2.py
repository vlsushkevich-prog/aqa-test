def filter_lines(path, keyword):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                yield line.strip()

for line in filter_lines('/Users/vlad/Desktop/Новая папка/report_old.txt', 'ERROR'):
    print(line)
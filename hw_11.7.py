def parse_int_list(strings):
    ints = []
    for s in strings:
        try:
            ints.append(int(s))
        except ValueError:
            print(f'Пропущено {s}')
            continue
    return ints

raw = ['10', '20', 'abc', '30', '4.5', '40']
nums = parse_int_list(raw)
print(nums)